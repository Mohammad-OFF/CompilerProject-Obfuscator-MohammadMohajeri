# obfuscator_passes.py
import random
import string
import ast_nodes as ast # Assuming your AST nodes are in ast_nodes.py

# --- Helper for generating new names ---
class NameGenerator:
    def __init__(self, prefix="obf_"):
        self.prefix = prefix
        self.used_names = set()
        self.counter = 0

    def new_name(self, original_name=""): # original_name can be used for hints if needed
        name = ""
        while not name or name in self.used_names:
            self.counter += 1
            name = f"{self.prefix}{self.counter}"
        self.used_names.add(name)
        return name

    def reset(self):
        self.used_names = set()
        self.counter = 0

# --- Obfuscation Pass Base Class ---
class ObfuscationPass:
    def __init__(self):
        self.name_gen = NameGenerator()

    def visit(self, node, symbol_map=None, **kwargs):
        if node is None:
            return None
        
        method_name = 'visit_' + node.__class__.__name__.lower()
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node, symbol_map, **kwargs)

    def generic_visit(self, node, symbol_map=None, **kwargs):
        # Iterate over attributes that might be single AST nodes or lists of AST nodes
        for attr_name in dir(node):
            if not attr_name.startswith('_') and attr_name not in ['line_no', 'parent', 'temp_local_scope_map']:
                try:
                    attr_value = getattr(node, attr_name)
                    if isinstance(attr_value, ast.Node):
                        new_child = self.visit(attr_value, symbol_map, **kwargs)
                        if new_child is not attr_value: # Reassign if a new node instance was returned
                             setattr(node, attr_name, new_child)
                    elif isinstance(attr_value, list):
                        # Process lists, potentially replacing nodes within the list
                        new_list_content = []
                        changed = False
                        for item in attr_value:
                            if isinstance(item, ast.Node):
                                visited_item = self.visit(item, symbol_map, **kwargs)
                                new_list_content.append(visited_item)
                                if visited_item is not item:
                                    changed = True
                            else:
                                new_list_content.append(item) # Keep non-node items
                        
                        if changed: # Only reassign list if content might have changed instance
                            # This is tricky: setattr(node, attr_name, new_list_content) might not always work as expected
                            # if the list itself should be modified in-place.
                            # For now, let's assume we can reassign the attribute.
                            # A safer way for lists is often to modify them in-place if possible,
                            # or clear and extend: attr_value.clear(); attr_value.extend(new_list_content)
                            setattr(node, attr_name, new_list_content)
                except AttributeError:
                    pass # Some attributes might not be relevant
        return node

    def apply(self, ast_root):
        raise NotImplementedError("Each obfuscation pass must implement 'apply'")

# --- 1. Identifier Renaming Pass ---
class IdentifierRenamingPass(ObfuscationPass):
    def __init__(self, rename_functions=True, rename_variables=True, rename_parameters=True):
        super().__init__()
        self.rename_functions = rename_functions
        self.rename_variables = rename_variables
        self.rename_parameters = rename_parameters
        self.global_symbol_map = {}

    def apply(self, ast_root):
        self.name_gen.reset()
        self.global_symbol_map = {}
        self.visit(ast_root, is_definition_phase=True)
        self.visit(ast_root, is_definition_phase=False)
        return ast_root

    def visit_programnode(self, node, symbol_map=None, **kwargs):
        if node.declarations:
            for i in range(len(node.declarations)):
                node.declarations[i] = self.visit(node.declarations[i], symbol_map, **kwargs)
        return node

    def visit_functiondefnode(self, node, symbol_map=None, **kwargs):
        is_definition_phase = kwargs.get('is_definition_phase')
        original_func_name = node.name.name
        
        if is_definition_phase:
            if self.rename_functions and original_func_name not in self.global_symbol_map:
                if original_func_name not in ["main", "printf", "scanf"]: # Exclude built-ins/entry
                    self.global_symbol_map[original_func_name] = self.name_gen.new_name(original_func_name)
            
            current_function_local_map = {}
            if self.rename_parameters and node.params:
                for param in node.params:
                    if param.name and param.name.name: # Ensure param and its name exist
                         original_param_name = param.name.name
                         current_function_local_map[original_param_name] = self.name_gen.new_name(original_param_name)
            
            if self.rename_variables and node.body:
                self._collect_local_vars_for_map(node.body, current_function_local_map)
            node.temp_local_scope_map = current_function_local_map # Attach map to node
        
        else: # Application phase
            if self.rename_functions and original_func_name in self.global_symbol_map:
                node.name.name = self.global_symbol_map[original_func_name]

            retrieved_local_map = getattr(node, 'temp_local_scope_map', {})
            
            if self.rename_parameters and node.params:
                for i in range(len(node.params)):
                    # ParamNode itself needs to be visited to rename its IdentifierNode (name)
                    node.params[i] = self.visit(node.params[i], symbol_map, current_function_scope_map=retrieved_local_map, **kwargs)

            if node.body:
                body_kwargs = kwargs.copy()
                body_kwargs['current_function_scope_map'] = retrieved_local_map
                node.body = self.visit(node.body, symbol_map, **body_kwargs)
        return node

    def _collect_local_vars_for_map(self, node_to_scan, local_map): # Renamed arg
        if isinstance(node_to_scan, ast.BlockNode) and node_to_scan.statements:
            for stmt in node_to_scan.statements:
                self._collect_local_vars_for_map(stmt, local_map)
        elif isinstance(node_to_scan, ast.VarDeclNode):
            if node_to_scan.name and node_to_scan.name.name: # Check name exists
                original_var_name = node_to_scan.name.name
                if original_var_name not in local_map:
                    local_map[original_var_name] = self.name_gen.new_name(original_var_name)
        elif isinstance(node_to_scan, ast.IfNode):
            if node_to_scan.then_block: self._collect_local_vars_for_map(node_to_scan.then_block, local_map)
            if node_to_scan.else_block: self._collect_local_vars_for_map(node_to_scan.else_block, local_map)
        elif isinstance(node_to_scan, ast.WhileNode) and node_to_scan.body:
            self._collect_local_vars_for_map(node_to_scan.body, local_map)
        elif isinstance(node_to_scan, ast.ForNode):
            if node_to_scan.init and isinstance(node_to_scan.init, ast.VarDeclNode):
                self._collect_local_vars_for_map(node_to_scan.init, local_map) # Var in for-init
            if node_to_scan.body: self._collect_local_vars_for_map(node_to_scan.body, local_map)

    def visit_paramnode(self, node, symbol_map=None, **kwargs):
        is_definition_phase = kwargs.get('is_definition_phase')
        current_function_scope_map = kwargs.get('current_function_scope_map')
        if not is_definition_phase and self.rename_parameters:
            if current_function_scope_map and node.name and node.name.name in current_function_scope_map:
                node.name.name = current_function_scope_map[node.name.name]
        # TypeNode does not need renaming
        # node.param_type = self.visit(node.param_type, ...) # If types could be complex/renamed
        return node

    def visit_vardeclnode(self, node, symbol_map=None, **kwargs):
        is_definition_phase = kwargs.get('is_definition_phase')
        current_function_scope_map = kwargs.get('current_function_scope_map')

        if not is_definition_phase and self.rename_variables:
            if current_function_scope_map and node.name and node.name.name in current_function_scope_map:
                node.name.name = current_function_scope_map[node.name.name]
        
        if node.initializer:
            node.initializer = self.visit(node.initializer, symbol_map, **kwargs)
        # node.var_type = self.visit(node.var_type, ...) # If type could be complex
        return node
            
    def visit_identifiernode(self, node, symbol_map=None, **kwargs):
        is_definition_phase = kwargs.get('is_definition_phase')
        current_function_scope_map = kwargs.get('current_function_scope_map')

        if not is_definition_phase and node.name: # Check if name exists
            original_id_name = node.name
            if current_function_scope_map and original_id_name in current_function_scope_map:
                node.name = current_function_scope_map[original_id_name]
            elif original_id_name in self.global_symbol_map: # Check global map (for function calls)
                if original_id_name not in ["printf", "scanf"]: # Don't rename built-ins by mistake
                    node.name = self.global_symbol_map[original_id_name]
        return node

    def visit_functioncallnode(self, node, symbol_map=None, **kwargs):
        # The function name itself is an IdentifierNode, so it will be handled by visit_identifiernode
        # when we visit node.name
        if node.name:
            node.name = self.visit(node.name, symbol_map, **kwargs) # Pass all kwargs including scope map
        
        if node.args:
            new_args = []
            for arg in node.args:
                visited_arg = self.visit(arg, symbol_map, **kwargs) # Pass all kwargs
                if visited_arg is not None:
                    new_args.append(visited_arg)
            node.args = new_args
        return node

    def visit_assignmentnode(self, node, symbol_map=None, **kwargs):
        if node.lvalue: node.lvalue = self.visit(node.lvalue, symbol_map, **kwargs)
        if node.rvalue: node.rvalue = self.visit(node.rvalue, symbol_map, **kwargs)
        return node

    def visit_ifnode(self, node, symbol_map=None, **kwargs):
        if node.condition: node.condition = self.visit(node.condition, symbol_map, **kwargs)
        if node.then_block: node.then_block = self.visit(node.then_block, symbol_map, **kwargs)
        if node.else_block: node.else_block = self.visit(node.else_block, symbol_map, **kwargs)
        return node

    def visit_whilenode(self, node, symbol_map=None, **kwargs):
        if node.condition: node.condition = self.visit(node.condition, symbol_map, **kwargs)
        if node.body: node.body = self.visit(node.body, symbol_map, **kwargs)
        return node

    def visit_fornode(self, node, symbol_map=None, **kwargs):
        if node.init: node.init = self.visit(node.init, symbol_map, **kwargs)
        if node.condition: node.condition = self.visit(node.condition, symbol_map, **kwargs)
        if node.update: node.update = self.visit(node.update, symbol_map, **kwargs)
        if node.body: node.body = self.visit(node.body, symbol_map, **kwargs)
        return node

    def visit_returnnode(self, node, symbol_map=None, **kwargs):
        if node.expr:
            node.expr = self.visit(node.expr, symbol_map, **kwargs)
        return node

    def visit_binaryopnode(self, node, symbol_map=None, **kwargs):
        if node.left: node.left = self.visit(node.left, symbol_map, **kwargs)
        if node.right: node.right = self.visit(node.right, symbol_map, **kwargs)
        return node

    def visit_unaryopnode(self, node, symbol_map=None, **kwargs):
        if node.expr: node.expr = self.visit(node.expr, symbol_map, **kwargs)
        return node

    def visit_blocknode(self, node, symbol_map=None, **kwargs):
        if node.statements:
            for i in range(len(node.statements)):
                 node.statements[i] = self.visit(node.statements[i], symbol_map, **kwargs)
        return node

    def visit_exprstatementnode(self, node, symbol_map=None, **kwargs):
        if node.expr: node.expr = self.visit(node.expr, symbol_map, **kwargs)
        return node

    def visit_typenode(self, node, symbol_map=None, **kwargs): return node
    def visit_numberliteralnode(self, node, symbol_map=None, **kwargs): return node
    def visit_charliteralnode(self, node, symbol_map=None, **kwargs): return node
    def visit_stringliteralnode(self, node, symbol_map=None, **kwargs): return node
    def visit_boolliteralnode(self, node, symbol_map=None, **kwargs): return node


# --- 2. Dead Code Insertion Pass ---
class DeadCodeInsertionPass(ObfuscationPass):
    def __init__(self, probability=0.25):
        super().__init__()
        self.probability = probability

    def apply(self, ast_root):
        self.name_gen.reset()
        self.visit(ast_root) # Pass ast_root, symbol_map=None, **kwargs (empty kwargs ok for this pass)
        return ast_root

    def _create_random_dead_statement(self):
        var_name = self.name_gen.new_name("unused_var_")
        rand_val = random.randint(-10000, 10000)
        dead_var_decl = ast.VarDeclNode(
            var_type=ast.TypeNode("int"),
            name=ast.IdentifierNode(var_name),
            initializer=ast.NumberLiteralNode(rand_val)
        )
        return dead_var_decl

    def visit_blocknode(self, node, symbol_map=None, **kwargs):
        if node.statements is not None:
            new_statements = []
            for stmt in node.statements:
                # Visit the original statement first, in case it's a block itself
                # and dead code needs to be inserted within it.
                visited_stmt = self.visit(stmt, symbol_map, **kwargs)
                new_statements.append(visited_stmt)
                
                if not isinstance(visited_stmt, ast.ReturnNode) and random.random() < self.probability:
                    dead_stmt = self._create_random_dead_statement()
                    if dead_stmt:
                        new_statements.append(dead_stmt)
            node.statements = new_statements
        return node

    # Need to ensure that complex statements containing blocks are visited so their blocks can be processed.
    def visit_functiondefnode(self, node, symbol_map=None, **kwargs):
        if node.body: node.body = self.visit(node.body, symbol_map, **kwargs)
        return node

    def visit_ifnode(self, node, symbol_map=None, **kwargs):
        # For dead code, we only care about transforming blocks, not expressions
        if node.then_block: node.then_block = self.visit(node.then_block, symbol_map, **kwargs)
        if node.else_block: node.else_block = self.visit(node.else_block, symbol_map, **kwargs)
        return node

    def visit_whilenode(self, node, symbol_map=None, **kwargs):
        if node.body: node.body = self.visit(node.body, symbol_map, **kwargs)
        return node

    def visit_fornode(self, node, symbol_map=None, **kwargs):
        if node.body: node.body = self.visit(node.body, symbol_map, **kwargs)
        return node
    
    # Other node types can rely on generic_visit for this pass if they don't directly manage blocks
    # or don't need special handling for dead code insertion.

# --- Main Obfuscator Class ---
class Obfuscator:
    def __init__(self, techniques=None):
        self.passes = []
        if techniques is None:
            techniques = ["rename_identifiers", "dead_code"]

        if "rename_identifiers" in techniques:
            self.passes.append(IdentifierRenamingPass())
        if "dead_code" in techniques:
            self.passes.append(DeadCodeInsertionPass(probability=0.25))
        # Add more passes here based on the 'techniques' list
        # e.g., if "complicate_expressions" in techniques: self.passes.append(ExpressionComplicationPass())

    def apply_passes(self, ast_root):
        current_ast = ast_root
        for p_instance in self.passes:
            print(f"Applying pass: {p_instance.__class__.__name__}")
            current_ast = p_instance.apply(current_ast) 
            if current_ast is None:
                print(f"Error: Pass {p_instance.__class__.__name__} returned None. Reverting to original AST for this pass.")
                # This indicates a bug in the pass; ideally, it should always return an AST node.
                # For safety, one might return the AST state before this pass, but that's complex to manage here.
                # Simplest is to stop or return the original ast_root.
                return ast_root # Or raise an error
        return current_ast