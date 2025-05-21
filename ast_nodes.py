class Node:
    """Base class for all AST nodes."""

    def __init__(self, line_no=None):
        self.line_no = line_no


class ProgramNode(Node):
    def __init__(self, declarations, line_no=None):
        super().__init__(line_no)
        self.declarations = declarations


class FunctionDefNode(Node):
    def __init__(self, return_type, name, params, body, line_no=None):
        super().__init__(line_no)
        self.return_type = return_type
        self.name = name
        self.params = params
        self.body = body
        self.temp_local_scope_map = {}


class ParamNode(Node):
    def __init__(self, param_type, name, line_no=None):
        super().__init__(line_no)
        self.param_type = param_type
        self.name = name


class TypeNode(Node):
    def __init__(self, type_name, line_no=None):
        super().__init__(line_no)
        self.type_name = type_name


class BlockNode(Node):
    def __init__(self, statements, line_no=None):
        super().__init__(line_no)
        self.statements = statements


class VarDeclNode(Node):
    def __init__(self, var_type, name, initializer=None, line_no=None):
        super().__init__(line_no)
        self.var_type = var_type
        self.name = name
        self.initializer = initializer


class AssignmentNode(Node):
    def __init__(self, lvalue, rvalue, line_no=None):
        super().__init__(line_no)
        self.lvalue = lvalue
        self.rvalue = rvalue


class IfNode(Node):
    def __init__(self, condition, then_block, else_block=None, line_no=None):
        super().__init__(line_no)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block


class WhileNode(Node):
    def __init__(self, condition, body, line_no=None):
        super().__init__(line_no)
        self.condition = condition
        self.body = body


class ForNode(Node):
    def __init__(self, init, condition, update, body, line_no=None):
        super().__init__(line_no)
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body


class ReturnNode(Node):
    def __init__(self, expr=None, line_no=None):
        super().__init__(line_no)
        self.expr = expr


class FunctionCallNode(Node):
    def __init__(self, name, args, line_no=None):
        super().__init__(line_no)
        self.name = name
        self.args = args


class ExprStatementNode(Node):
    def __init__(self, expr, line_no=None):
        super().__init__(line_no)
        self.expr = expr



class BinaryOpNode(Node):
    def __init__(self, left, op, right, line_no=None):
        super().__init__(line_no)
        self.left = left
        self.op = op
        self.right = right


class UnaryOpNode(Node):
    def __init__(self, op, expr, line_no=None):
        super().__init__(line_no)
        self.op = op
        self.expr = expr


class IdentifierNode(Node):
    def __init__(self, name, line_no=None):
        super().__init__(line_no)
        self.name = name


class NumberLiteralNode(Node):
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value


class CharLiteralNode(Node):
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value


class StringLiteralNode(Node):
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value


class BoolLiteralNode(Node):
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value