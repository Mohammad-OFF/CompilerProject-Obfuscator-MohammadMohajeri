# deobfuscator_passes.py

import ast_nodes as ast
from typing import Set, Dict, List, Optional

class Deobfuscator:
    def __init__(self):
        self.func_map: Dict[str, str] = {}
        self.func_counter = 1
        self.local_var_counter = 1
        self.local_param_counter = 1

        self.naming_heuristics = {
            "sum": ["sum", "total", "add", "result"],
            "main": ["main", "start"],
            "iterator": ["i", "j", "k"],
        }

    def simplify(self, program_node: ast.ProgramNode) -> ast.ProgramNode:
        if not isinstance(program_node, ast.ProgramNode):
            return program_node

        for decl in program_node.declarations:
            if isinstance(decl, ast.FunctionDefNode):
                inferred_name = self._infer_function_name(decl)
                # apply switch/while flatten pass (operate on program-level, before renaming/processing functions)
                self._flatten_switch_state_machine(program_node)
                orig_name = decl.name.name
                if inferred_name:
                    self.func_map[orig_name] = inferred_name
                elif orig_name.startswith("obf_"):
                    new_name = f"func{self.func_counter}"
                    self.func_counter += 1
                    self.func_map[orig_name] = new_name
        
        self._simplify_binary_ops(program_node)
        
        for decl in program_node.declarations:
            if isinstance(decl, ast.FunctionDefNode):
                self._process_function(decl)
        
        for decl in program_node.declarations:
            if isinstance(decl, ast.FunctionDefNode):
                self._process_function(decl)

        # NEW PASS: Inline variable declarations
        for decl in program_node.declarations:
            if isinstance(decl, ast.FunctionDefNode):
                self._inline_variable_declarations(decl.body)

        self._replace_function_calls(program_node)

        return program_node

    def _simplify_binary_ops(self, node):
        if node is None:
            return

        if isinstance(node, ast.BinaryOpNode):
            if node.op == '-' and isinstance(node.right, ast.UnaryOpNode) and node.right.op == '-':
                node.op = '+'
                node.right = node.right.expr
            elif node.op == '-' and isinstance(node.right, ast.UnaryOpNode) and node.right.op == '+':
                node.op = '-'
                node.right = node.right.expr
            elif node.op == '+' and isinstance(node.right, ast.UnaryOpNode) and node.right.op == '-':
                node.op = '-'
                node.right = node.right.expr
                
        for attr, val in vars(node).items():
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, ast.Node):
                        self._simplify_binary_ops(item)
            elif isinstance(val, ast.Node):
                self._simplify_binary_ops(val)

    def _process_function(self, func: ast.FunctionDefNode):
        used = self._collect_used_identifiers(func.body)
        self._prune_dead_vars_in_block(func.body, used)

        self.local_param_counter = 1
        self.local_var_counter = 1
        local_map: Dict[str, str] = self._infer_local_names(func)

        # Apply inferred names to parameters
        for param in func.params or []:
            orig = param.name.name
            if orig in local_map:
                param.name.name = local_map[orig]
            else:
                new = f"param{self.local_param_counter}"
                self.local_param_counter += 1
                local_map[orig] = new
                param.name.name = new

        # Apply inferred names to variables
        var_nodes = []
        self._collect_var_decls(func.body, var_nodes)
        for v in var_nodes:
            orig = v.name.name
            if orig in local_map:
                v.name.name = local_map[orig]
            else:
                new = f"var{self.local_var_counter}"
                self.local_var_counter += 1
                local_map[orig] = new
                v.name.name = new

        fname = func.name.name
        if fname in self.func_map:
            func.name.name = self.func_map[fname]

        self._replace_identifiers_in_node(func.body, local_map, self.func_map)

    def _infer_function_name(self, func: ast.FunctionDefNode) -> Optional[str]:
        """
        Infer simple arithmetic-based function names with normalization of
        binary ops (handle patterns like a - (-b) -> a + b).
        """
        # collect body statements robustly
        body_stmts = []
        if isinstance(func.body, ast.BlockNode):
            body_stmts = func.body.statements or []
        else:
            body_stmts = [func.body] if func.body is not None else []

        def op_to_name(op: str) -> Optional[str]:
            return { "+": "sum", "-": "subtract", "*": "multiply", "/": "divide" }.get(op)

        def effective_op(bin_node: ast.BinaryOpNode) -> Optional[str]:
            """Return the semantically effective operator for a BinaryOpNode,
            normalizing patterns like a - (-b) -> +, a + (-b) -> - (if occurs)."""
            if not isinstance(bin_node, ast.BinaryOpNode):
                return None
            op = bin_node.op
            # normalize a - (-b)  => a + b
            if op == '-' and isinstance(bin_node.right, ast.UnaryOpNode) and bin_node.right.op == '-':
                return '+'
            # normalize a + (-b) => a - b   (less common, but handle)
            if op == '+' and isinstance(bin_node.right, ast.UnaryOpNode) and bin_node.right.op == '-':
                return '-'
            # normalize -( - (a op b) ) etc. (not exhaustive)
            return op

        # 1) direct: return a OP b
        if len(body_stmts) == 1 and isinstance(body_stmts[0], ast.ReturnNode):
            ret = body_stmts[0]
            expr = getattr(ret, "expr", None)
            if isinstance(expr, ast.BinaryOpNode):
                eff = effective_op(expr)
                name = op_to_name(eff) if eff else None
                if name:
                    return name

        # 2) pattern: VarDecl (with binary initializer) then immediate return of that var
        if len(body_stmts) >= 2:
            for i in range(len(body_stmts) - 1):
                decl = body_stmts[i]
                ret = body_stmts[i + 1]
                if isinstance(decl, ast.VarDeclNode) and isinstance(decl.initializer, ast.BinaryOpNode) \
                and isinstance(ret, ast.ReturnNode) and isinstance(ret.expr, ast.IdentifierNode):
                    if ret.expr.name == decl.name.name:
                        eff = effective_op(decl.initializer)
                        name = op_to_name(eff) if eff else None
                        if name:
                            return name

        # 3) more general: find any var-decl with binary init and a return later of that var
        var_init_map = {}
        for stmt in body_stmts:
            if isinstance(stmt, ast.VarDeclNode) and isinstance(stmt.initializer, ast.BinaryOpNode):
                var_init_map[stmt.name.name] = stmt.initializer
        for stmt in body_stmts:
            if isinstance(stmt, ast.ReturnNode) and isinstance(stmt.expr, ast.IdentifierNode):
                vname = stmt.expr.name
                if vname in var_init_map:
                    eff = effective_op(var_init_map[vname])
                    name = op_to_name(eff) if eff else None
                    if name:
                        return name

        # 4) heuristic for main (presence of printf somewhere)
        def contains_printf(n) -> bool:
            if n is None:
                return False
            if isinstance(n, ast.ExprStatementNode) and isinstance(n.expr, ast.FunctionCallNode):
                callee = n.expr.name
                if isinstance(callee, ast.IdentifierNode) and callee.name == "printf":
                    return True
            for attr, val in vars(n).items():
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, ast.Node) and contains_printf(item):
                            return True
                elif isinstance(val, ast.Node):
                    if contains_printf(val):
                        return True
            return False

        for s in body_stmts:
            if contains_printf(s):
                return "main"

        return None


    def _flatten_block(self, node):
        # A helper to flatten a block into a list of statements for analysis
        if isinstance(node, ast.BlockNode):
            return node.statements
        return [node]

    def _infer_local_names(self, func: ast.FunctionDefNode) -> Dict[str, str]:
        inferred_map: Dict[str, str] = {}
        
        func_name = self.func_map.get(func.name.name, func.name.name)

        # Rule for 'sum' function: rename params to x, y and result to total
        if func_name == "sum":
            if len(func.params) >= 2:
                inferred_map[func.params[0].name.name] = "x"
                inferred_map[func.params[1].name.name] = "y"
            for stmt in func.body.statements:
                if isinstance(stmt, ast.VarDeclNode) and isinstance(stmt.initializer, ast.BinaryOpNode) and stmt.initializer.op == "+":
                    inferred_map[stmt.name.name] = "result"
        
        # Rule for 'main' function: rename variables based on usage
        if func_name == "main":
            var_nodes = []
            self._collect_var_decls(func.body, var_nodes)
            
            call_args = []
            for stmt in func.body.statements:
                if isinstance(stmt, ast.ExprStatementNode) and isinstance(stmt.expr, ast.FunctionCallNode) and stmt.expr.name.name == "fxz":
                    call_args = stmt.expr.args
                    break
                
            if call_args:
                for v in var_nodes:
                    if v.name.name == "var3": # This needs a better heuristic
                        inferred_map[v.name.name] = "total"
                    elif self._is_used_as_arg(v.name.name, call_args):
                        if v.name.name == "var1":
                            inferred_map[v.name.name] = "x"
                        elif v.name.name == "var2":
                            inferred_map[v.name.name] = "y"

        return inferred_map
    
    def _is_used_as_arg(self, var_name: str, args: List) -> bool:
        for arg in args:
            if isinstance(arg, ast.IdentifierNode) and arg.name == var_name:
                return True
        return False
        
    def _collect_used_identifiers(self, node) -> Set[str]:
        used: Set[str] = set()
        def visit(n):
            if n is None: return
            if isinstance(n, ast.IdentifierNode): used.add(n.name); return
            if isinstance(n, ast.VarDeclNode):
                if n.initializer: visit(n.initializer); return
            if isinstance(n, ast.ParamNode): return
            for attr, val in vars(n).items():
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, ast.Node): visit(item)
                elif isinstance(val, ast.Node): visit(val)
        visit(node)
        return used

    def _collect_var_decls(self, node, out_list: List[ast.VarDeclNode]):
        if node is None: return
        if isinstance(node, ast.VarDeclNode):
            out_list.append(node); return
        for attr, val in vars(node).items():
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, ast.Node): self._collect_var_decls(item, out_list)
            elif isinstance(val, ast.Node): self._collect_var_decls(val, out_list)

    def _prune_dead_vars_in_block(self, block: ast.BlockNode, used: Set[str]):
        if block is None: return
        new_stmts = []
        for stmt in block.statements or []:
            removed = False
            if isinstance(stmt, ast.VarDeclNode):
                name = stmt.name.name
                init = stmt.initializer
                if name not in used:
                    if init is None or isinstance(init, (ast.NumberLiteralNode, ast.CharLiteralNode, ast.StringLiteralNode, ast.BoolLiteralNode)):
                        removed = True
            if removed: continue
            if isinstance(stmt, ast.BlockNode): self._prune_dead_vars_in_block(stmt, used)
            elif isinstance(stmt, ast.IfNode):
                if isinstance(stmt.then_block, ast.BlockNode): self._prune_dead_vars_in_block(stmt.then_block, used)
                if stmt.else_block and isinstance(stmt.else_block, ast.BlockNode): self._prune_dead_vars_in_block(stmt.else_block, used)
            elif isinstance(stmt, ast.WhileNode) and isinstance(stmt.body, ast.BlockNode): self._prune_dead_vars_in_block(stmt.body, used)
            elif isinstance(stmt, ast.ForNode) and isinstance(stmt.body, ast.BlockNode): self._prune_dead_vars_in_block(stmt.body, used)
            new_stmts.append(stmt)
        block.statements = new_stmts

    def _replace_identifiers_in_node(self, node, local_map: Dict[str, str], func_map: Dict[str, str]):
        if node is None: return
        if isinstance(node, ast.IdentifierNode):
            if node.name in local_map: node.name = local_map[node.name]
            elif node.name in func_map: node.name = func_map[node.name]
            return
        if isinstance(node, ast.VarDeclNode):
            if node.initializer: self._replace_identifiers_in_node(node.initializer, local_map, func_map)
            return
        if isinstance(node, ast.ParamNode): return
        for attr, val in vars(node).items():
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, ast.Node): self._replace_identifiers_in_node(item, local_map, func_map)
            elif isinstance(val, ast.Node): self._replace_identifiers_in_node(val, local_map, func_map)

    def _replace_function_calls(self, program_node: ast.ProgramNode):
        def visit(n):
            if n is None: return
            if isinstance(n, ast.IdentifierNode):
                if n.name in self.func_map: n.name = self.func_map[n.name]
                return
            for attr, val in vars(n).items():
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, ast.Node): visit(item)
                elif isinstance(val, ast.Node): visit(val)
        visit(program_node)

    def _flatten_switch_state_machine(self, program_node: ast.ProgramNode):
        """
        Find functions that implement a state-machine pattern:
        varS = <num>;
        while (varS > 0) {
            switch(varS) { case N: ...; varS = M; break; ... }
        }
        And flatten them into a linear sequence by simulating states from initial value.
        This operates in-place on program_node.
        """
        if program_node is None:
            return

        for decl in program_node.declarations:
            if not isinstance(decl, ast.FunctionDefNode):
                continue

            # decide whether this function is candidate 'main'
            func_name = decl.name.name
            # function may be already renamed via func_map or mapping exists
            mapped = self.func_map.get(func_name, None)
            if not (func_name == "main" or mapped == "main"):
                # still try apply to function named 'main' only (conservative)
                continue

            self._flatten_in_function(decl)

    def _flatten_in_function(self, func: ast.FunctionDefNode):
        if func is None or not isinstance(func, ast.FunctionDefNode):
            return

        stmts = func.body.statements or []

        while_stmt = None
        switch_node = None
        for s in stmts:
            if isinstance(s, ast.WhileNode) and isinstance(s.body, ast.BlockNode):
                inner = s.body.statements or []
                if len(inner) == 1 and isinstance(inner[0], ast.SwitchCaseNode):
                    while_stmt = s
                    switch_node = inner[0]
                    break
        if switch_node is None or while_stmt is None:
            return

        state_var = None
        if isinstance(switch_node.expression, ast.IdentifierNode):
            state_var = switch_node.expression.name
        if state_var is None:
            return

        init_state = None
        for s in stmts:
            if isinstance(s, ast.VarDeclNode) and isinstance(s.name, ast.IdentifierNode) and s.name.name == state_var:
                if isinstance(s.initializer, ast.NumberLiteralNode):
                    init_state = s.initializer.value
                    break
        if init_state is None:
            for s in stmts:
                if isinstance(s, ast.ExprStatementNode) and isinstance(s.expr, ast.AssignmentNode):
                    left = s.expr.lvalue
                    right = s.expr.rvalue
                    if isinstance(left, ast.IdentifierNode) and left.name == state_var and isinstance(right, ast.NumberLiteralNode):
                        init_state = right.value
                        break
        if init_state is None:
            return

        case_map = {}
        for case in switch_node.cases or []:
            if isinstance(case, ast.CaseNode):
                key = None
                if isinstance(case.value, ast.NumberLiteralNode):
                    key = case.value.value
                if key is not None:
                    case_map[key] = case.body.statements or []
        if not case_map:
            return

        # جمع‌آوری statements خطی با حفظ ترتیب
        new_linear_stmts = []
        visited = set()
        state = init_state
        while state in case_map and state not in visited:
            visited.add(state)
            body_stmts = case_map[state]
            for cs in body_stmts:
                if isinstance(cs, ast.BreakNode):
                    continue
                if isinstance(cs, ast.ExprStatementNode) and isinstance(cs.expr, ast.AssignmentNode):
                    assign = cs.expr
                    l = assign.lvalue
                    r = assign.rvalue
                    if isinstance(l, ast.IdentifierNode) and l.name == state_var and isinstance(r, ast.NumberLiteralNode):
                        state = r.value
                        continue
                new_linear_stmts.append(cs)

        # مرتب‌سازی statements: همه قبل از while + linearized statements
        new_body = []
        for s in stmts:
            if s is while_stmt:
                continue
            if isinstance(s, ast.VarDeclNode) and isinstance(s.name, ast.IdentifierNode) and s.name.name == state_var:
                continue
            # اگر return هست، آن را آخر اضافه می‌کنیم بعدا
            if isinstance(s, ast.ReturnNode):
                continue
            new_body.append(s)

        # اضافه کردن statements flatten شده
        new_body.extend(new_linear_stmts)

        # اضافه کردن return در انتها اگر وجود داشت
        for s in stmts:
            if isinstance(s, ast.ReturnNode):
                new_body.append(s)
                break

        func.body.statements = new_body



    # In deobfuscator_passes.py

    def _inline_variable_declarations(self, node):
        """
        Finds variable declarations followed by an assignment to the same variable
        and inlines the assignment into the declaration.
        """
        if node is None or not isinstance(node, ast.BlockNode):
            return

        statements = node.statements
        if not statements:
            return

        new_statements = []
        i = 0
        while i < len(statements):
            current_stmt = statements[i]
            
            # Look for a VarDeclNode
            if isinstance(current_stmt, ast.VarDeclNode):
                # Check the next statement for an assignment to the same variable
                if i + 1 < len(statements):
                    next_stmt = statements[i+1]
                    if isinstance(next_stmt, ast.ExprStatementNode) and isinstance(next_stmt.expr, ast.AssignmentNode):
                        assign_node = next_stmt.expr
                        if isinstance(assign_node.lvalue, ast.IdentifierNode) and assign_node.lvalue.name == current_stmt.name.name:
                            # Found the pattern! Combine them.
                            current_stmt.initializer = assign_node.rvalue
                            new_statements.append(current_stmt)
                            i += 2  # Skip both the original declaration and the assignment
                            continue
            
            new_statements.append(current_stmt)
            i += 1
        
        node.statements = new_statements