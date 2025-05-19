# ast_nodes.py

class Node:
    """Base class for all AST nodes."""
    def __init__(self, line_no=None):
        self.line_no = line_no # Optional: store line number for error reporting or debugging

    # The 'accept' method for the Visitor pattern can be added later if needed
    # by the obfuscator_passes or code_generator. It is not strictly
    # necessary for the AST structure itself.
    # def accept(self, visitor):
    #     method_name = 'visit_' + self.__class__.__name__.lower()
    #     visitor_method = getattr(visitor, method_name, visitor.generic_visit)
    #     return visitor_method(self)

class ProgramNode(Node):
    def __init__(self, declarations, line_no=None):
        super().__init__(line_no)
        self.declarations = declarations # List of FunctionDefNode (and potentially GlobalVarDeclNode)

class FunctionDefNode(Node):
    def __init__(self, return_type, name, params, body, line_no=None):
        super().__init__(line_no)
        self.return_type = return_type # TypeNode
        self.name = name               # IdentifierNode (holds the function name string)
        self.params = params           # List of ParamNode
        self.body = body               # BlockNode (representing the function's compound statement)
        # For IdentifierRenamingPass to store local scope map temporarily
        self.temp_local_scope_map = {}

class ParamNode(Node):
    def __init__(self, param_type, name, line_no=None):
        super().__init__(line_no)
        self.param_type = param_type   # TypeNode
        self.name = name               # IdentifierNode (holds the parameter name string)

class TypeNode(Node): # Represents a type like 'int', 'char', 'bool'
    def __init__(self, type_name, line_no=None):
        super().__init__(line_no)
        self.type_name = type_name     # String: "int", "char", "bool"

class BlockNode(Node): # Represents a compound statement: { statement* }
    def __init__(self, statements, line_no=None):
        super().__init__(line_no)
        self.statements = statements   # List of statement nodes

class VarDeclNode(Node): # Variable declaration: e.g., int x; or int x = 5;
    def __init__(self, var_type, name, initializer=None, line_no=None):
        super().__init__(line_no)
        self.var_type = var_type       # TypeNode
        self.name = name               # IdentifierNode
        self.initializer = initializer # Optional: ExpressionNode

class AssignmentNode(Node): # Assignment expression: lvalue = rvalue
    def __init__(self, lvalue, rvalue, line_no=None):
        super().__init__(line_no)
        self.lvalue = lvalue           # IdentifierNode (for simple Mini-C)
        self.rvalue = rvalue           # ExpressionNode

class IfNode(Node):
    def __init__(self, condition, then_block, else_block=None, line_no=None):
        super().__init__(line_no)
        self.condition = condition     # ExpressionNode
        self.then_block = then_block   # StatementNode (often a BlockNode)
        self.else_block = else_block   # Optional: StatementNode (often a BlockNode)

class WhileNode(Node):
    def __init__(self, condition, body, line_no=None):
        super().__init__(line_no)
        self.condition = condition     # ExpressionNode
        self.body = body               # StatementNode (often a BlockNode)

class ForNode(Node): # Mini-C for loop: for (init; condition; update) body
    def __init__(self, init, condition, update, body, line_no=None):
        super().__init__(line_no)
        self.init = init               # Optional: VarDeclNode or ExpressionNode (e.g., AssignmentNode)
        self.condition = condition     # Optional: ExpressionNode
        self.update = update           # Optional: ExpressionNode
        self.body = body               # StatementNode (often a BlockNode)

class ReturnNode(Node):
    def __init__(self, expr=None, line_no=None):
        super().__init__(line_no)
        self.expr = expr               # Optional: ExpressionNode

class FunctionCallNode(Node):
    def __init__(self, name, args, line_no=None):
        super().__init__(line_no)
        self.name = name               # IdentifierNode (function name)
        self.args = args               # List of ExpressionNode

class ExprStatementNode(Node): # Used when an expression is a statement itself (e.g. func_call(); or x=1;)
    def __init__(self, expr, line_no=None):
        super().__init__(line_no)
        self.expr = expr               # The expression being used as a statement

# --- Expression Nodes ---
class BinaryOpNode(Node): # For operators like +, -, *, /, ==, &&, etc.
    def __init__(self, left, op, right, line_no=None):
        super().__init__(line_no)
        self.left = left               # ExpressionNode
        self.op = op                   # String: the operator itself (e.g., "+", "==")
        self.right = right             # ExpressionNode

class UnaryOpNode(Node): # For operators like unary -, !
    def __init__(self, op, expr, line_no=None):
        super().__init__(line_no)
        self.op = op                   # String: the operator (e.g., "-", "!")
        self.expr = expr               # ExpressionNode

class IdentifierNode(Node): # Represents an identifier (variable name, function name)
    def __init__(self, name, line_no=None):
        super().__init__(line_no)
        self.name = name               # String: the identifier's name

class NumberLiteralNode(Node): # Integer literal
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value             # Integer value

class CharLiteralNode(Node): # Character literal e.g. 'a'
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value             # String (single character)

class StringLiteralNode(Node): # String literal e.g. "hello"
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value             # String

class BoolLiteralNode(Node): # Boolean literal: true or false
    def __init__(self, value, line_no=None):
        super().__init__(line_no)
        self.value = value             # Python boolean: True or False

# =============================================================================
# !!! NO OTHER CLASS DEFINITIONS (LIKE CodeGenerator) SHOULD BE IN THIS FILE !!!
# =============================================================================