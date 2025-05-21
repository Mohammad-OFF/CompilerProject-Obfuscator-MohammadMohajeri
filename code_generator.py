# code_generator.py
import ast_nodes as ast

class CodeGenerator:
    def __init__(self):
        self.indent_level = 0
        self.output_parts = [] # Use a list to join at the end for efficiency

    def _indent_str(self):
        return "    " * self.indent_level

    def _emit(self, *args):
        for arg in args:
            self.output_parts.append(str(arg))

    def _emit_line(self, *args): # Emits current indent, then args, then newline
        self._emit(self._indent_str())
        for arg in args:
            self._emit(arg)
        self._emit("\n")

    def generate(self, node): # THIS IS THE ENTRY POINT
        self.output_parts = []
        self.indent_level = 0
        if node:
            self.visit(node)
        return "".join(self.output_parts)

    def visit(self, node): # Generic dispatch method
        if node is None:
            return
        method_name = 'visit_' + node.__class__.__name__.lower()
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)

    def generic_visit(self, node):
        print(f"Warning: CodeGenerator has no specific visit method for {node.__class__.__name__}")
        self._emit(f"/* Unhandled AST node in CodeGenerator: {node.__class__.__name__} */")

    def visit_programnode(self, node: ast.ProgramNode):
        for i, decl in enumerate(node.declarations):
            self.visit(decl)
            if i < len(node.declarations) - 1:
                self._emit("\n") 

    def visit_functiondefnode(self, node: ast.FunctionDefNode):
        self._emit(self._indent_str()) 
        self.visit(node.return_type)
        self._emit(f" {node.name.name}(") 
        if node.params:
            for i, param in enumerate(node.params):
                self.visit(param)
                if i < len(node.params) - 1:
                    self._emit(", ")
        self._emit(") {\n") 
        self.indent_level += 1
        if node.body: 
            self.visit(node.body) 
        self.indent_level -= 1
        self._emit_line("}") 

    def visit_paramnode(self, node: ast.ParamNode):
        self.visit(node.param_type)
        self._emit(f" {node.name.name}") 

    def visit_typenode(self, node: ast.TypeNode):
        self._emit(node.type_name)

    def visit_blocknode(self, node: ast.BlockNode):
        if node.statements:
            for stmt in node.statements:
                self.visit(stmt)

    def visit_vardeclnode(self, node: ast.VarDeclNode):
        self._emit(self._indent_str()) 
        self.visit(node.var_type)
        self._emit(f" {node.name.name}") 
        if node.initializer:
            self._emit(" = ")
            self.visit(node.initializer)
        self._emit(";\n") 

    def visit_assignmentnode(self, node: ast.AssignmentNode):
        self.visit(node.lvalue) 
        self._emit(" = ")
        self.visit(node.rvalue)

    def visit_ifnode(self, node: ast.IfNode):
        self._emit(self._indent_str()) 
        self._emit("if (")
        self.visit(node.condition)
        self._emit(") ")
        
        if isinstance(node.then_block, ast.BlockNode):
            self._emit("{\n")
            self.indent_level += 1
            self.visit(node.then_block) 
            self.indent_level -= 1
            self._emit_line("}") 
        else: 
            self._emit("\n") 
            self.indent_level += 1
            self.visit(node.then_block) 
            self.indent_level -= 1

        if node.else_block:
            self._emit(self._indent_str() + "else ") 
            if isinstance(node.else_block, ast.BlockNode):
                self._emit("{\n")
                self.indent_level += 1
                self.visit(node.else_block)
                self.indent_level -= 1
                self._emit_line("}")
            else: 
                self._emit("\n")
                self.indent_level += 1
                self.visit(node.else_block)
                self.indent_level -= 1

    def visit_whilenode(self, node: ast.WhileNode):
        self._emit(self._indent_str())
        self._emit("while (")
        self.visit(node.condition)
        self._emit(") ")
        if isinstance(node.body, ast.BlockNode):
            self._emit("{\n")
            self.indent_level += 1
            self.visit(node.body)
            self.indent_level -= 1
            self._emit_line("}")
        else: 
            self._emit("\n")
            self.indent_level += 1
            self.visit(node.body)
            self.indent_level -= 1

    def visit_fornode(self, node: ast.ForNode):
        self._emit(self._indent_str())
        self._emit("for (")
        if node.init:
            if isinstance(node.init, ast.VarDeclNode):
                self.visit(node.init.var_type)
                self._emit(f" {node.init.name.name}")
                if node.init.initializer:
                    self._emit(" = ")
                    self.visit(node.init.initializer)
            else: 
                self.visit(node.init)
        self._emit("; ") 
        if node.condition:
            self.visit(node.condition)
        self._emit("; ") 
        if node.update:
            self.visit(node.update)
        self._emit(") ") 

        if isinstance(node.body, ast.BlockNode):
            self._emit("{\n")
            self.indent_level += 1
            self.visit(node.body)
            self.indent_level -= 1
            self._emit_line("}")
        else: 
            self._emit("\n")
            self.indent_level += 1
            self.visit(node.body)
            self.indent_level -= 1

    def visit_returnnode(self, node: ast.ReturnNode):
        self._emit(self._indent_str()) 
        self._emit("return")
        if node.expr:
            self._emit(" ")
            self.visit(node.expr)
        self._emit(";\n")

    def visit_functioncallnode(self, node: ast.FunctionCallNode):
        self.visit(node.name) 
        self._emit("(")
        if node.args:
            for i, arg in enumerate(node.args):
                self.visit(arg)
                if i < len(node.args) - 1:
                    self._emit(", ")
        self._emit(")")

    def visit_exprstatementnode(self, node: ast.ExprStatementNode):
        self._emit(self._indent_str()) 
        self.visit(node.expr)
        self._emit(";\n") 

    def visit_binaryopnode(self, node: ast.BinaryOpNode):
        is_left_complex = isinstance(node.left, ast.BinaryOpNode) 
        is_right_complex = isinstance(node.right, ast.BinaryOpNode)

        if is_left_complex: self._emit("(")
        self.visit(node.left)
        if is_left_complex: self._emit(")")

        self._emit(f" {node.op} ")

        if is_right_complex: self._emit("(")
        self.visit(node.right)
        if is_right_complex: self._emit(")")

    def visit_unaryopnode(self, node: ast.UnaryOpNode):
        self._emit(node.op)
        if isinstance(node.expr, ast.BinaryOpNode): 
             self._emit("(")
             self.visit(node.expr)
             self._emit(")")
        else:
             self.visit(node.expr)

    def visit_identifiernode(self, node: ast.IdentifierNode):
        self._emit(node.name)

    def visit_numberliteralnode(self, node: ast.NumberLiteralNode):
        self._emit(str(node.value))

    def visit_charliteralnode(self, node: ast.CharLiteralNode):
        val = node.value
        if val == "'": esc_val = "\\'"
        elif val == '\\': esc_val = '\\\\'
        elif val == '\n': esc_val = '\\n'
        elif val == '\t': esc_val = '\\t'
        elif val == '\r': esc_val = '\\r'
        else: esc_val = val
        self._emit(f"'{esc_val}'")

    def visit_stringliteralnode(self, node: ast.StringLiteralNode):
        escaped_value = node.value.replace('\\', '\\\\') \
                                  .replace('"', '\\"') \
                                  .replace('\n', '\\n') \
                                  .replace('\t', '\\t') \
                                  .replace('\r', '\\r')
        self._emit(f'"{escaped_value}"')

    def visit_boolliteralnode(self, node: ast.BoolLiteralNode):
        self._emit("true" if node.value else "false")