# ast_builder_visitor.py
from antlr4 import *

# Handle relative imports if this file is treated as part of a package structure
# or direct imports if it's a top-level script.
# This setup assumes 'generated_parser' is a subdirectory where ANTLR outputs its files.
if __name__ is not None and "." in __name__:
    # This case might be relevant if you structure your project more deeply as a Python package.
    # For a simple flat structure, the 'else' branch is more common.
    from .generated_parser.MiniCParser import MiniCParser
    from .generated_parser.MiniCVisitor import MiniCVisitor
else:
    # This assumes 'generated_parser' directory is in Python's search path
    # or you've added it (e.g. by having an __init__.py in project root and generated_parser,
    # or by manipulating sys.path, though direct relative often works if main.py is in root)
    # A common structure is:
    # project_root/
    #   main.py
    #   ast_builder_visitor.py
    #   ast_nodes.py
    #   ...
    #   generated_parser/
    #       MiniCParser.py
    #       MiniCVisitor.py
    #       ...
    # In this case, the imports below should work from main.py
    from generated_parser.MiniCParser import MiniCParser
    from generated_parser.MiniCVisitor import MiniCVisitor

import ast_nodes as custom_ast # Our existing AST node definitions

class ASTBuilderVisitor(MiniCVisitor):

    def get_line_number(self, ctx_or_token):
        if hasattr(ctx_or_token, 'start'): # It's a context object
            return ctx_or_token.start.line
        elif hasattr(ctx_or_token, 'symbol'): # It's a terminal node with a symbol
            return ctx_or_token.symbol.line
        elif hasattr(ctx_or_token, 'line'): # It might be a token itself
            return ctx_or_token.line
        return -1 # Default if line number cannot be determined

    # program: declaration+ EOF;
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        declarations = []
        for decl_ctx in ctx.declaration():
            declarations.append(self.visit(decl_ctx))
        # Filter out any None results if a visitDeclaration path could return None
        declarations = [d for d in declarations if d is not None]
        return custom_ast.ProgramNode(declarations, line_no=self.get_line_number(ctx))

    # declaration: functionDefinition;
    def visitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        if ctx.functionDefinition():
            return self.visit(ctx.functionDefinition())
        return None # Or raise error for unhandled declaration types

    # functionDefinition: typeSpecifier ID LPAREN parameters? RPAREN LBRACE blockContent RBRACE;
    def visitFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        return_type_node = self.visit(ctx.typeSpecifier())
        func_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        
        param_nodes = []
        if ctx.parameters():
            param_nodes = self.visit(ctx.parameters()) # visitParameters returns a list
            
        body_stmts_list = self.visit(ctx.blockContent()) # visitBlockContent returns a list
        body_block_node = custom_ast.BlockNode(body_stmts_list, line_no=self.get_line_number(ctx.LBRACE()))
        
        return custom_ast.FunctionDefNode(return_type_node, func_name_node, param_nodes, body_block_node, line_no=self.get_line_number(ctx))

    # typeSpecifier: INT | CHAR | BOOL;
    def visitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        type_name = ctx.getText()
        return custom_ast.TypeNode(type_name, line_no=self.get_line_number(ctx))

    # parameters: parameter (COMMA parameter)*;
    def visitParameters(self, ctx:MiniCParser.ParametersContext):
        params = []
        for param_ctx in ctx.parameter():
            params.append(self.visit(param_ctx))
        return params # Returns a list of ParamNode

    # parameter: typeSpecifier ID;
    def visitParameter(self, ctx:MiniCParser.ParameterContext):
        param_type_node = self.visit(ctx.typeSpecifier())
        param_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        return custom_ast.ParamNode(param_type_node, param_name_node, line_no=self.get_line_number(ctx))

    # blockContent: statement*;
    def visitBlockContent(self, ctx:MiniCParser.BlockContentContext):
        statements = []
        for stmt_ctx in ctx.statement():
            statements.append(self.visit(stmt_ctx))
        return statements # Returns a list of statement AST nodes

    # statement: ... | LBRACE blockContent RBRACE;
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        if ctx.variableDeclaration():
            # variableDeclaration rule itself doesn't have the SEMICOLON,
            # but the statement rule does: variableDeclaration SEMICOLON.
            # The VarDeclNode is built from visitVariableDeclaration.
            return self.visit(ctx.variableDeclaration())
        elif ctx.expression(): # This is for expression SEMICOLON
            expr_node = self.visit(ctx.expression())
            # We need to wrap raw expressions (like assignments or function calls if they are expressions)
            # in an ExprStatementNode if they are used as statements.
            return custom_ast.ExprStatementNode(expr_node, line_no=self.get_line_number(ctx))
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.returnStatement(): # returnStatement SEMICOLON
            return self.visit(ctx.returnStatement())
        elif ctx.LBRACE() and ctx.blockContent() and ctx.RBRACE(): # Nested block
            stmts_in_block = self.visit(ctx.blockContent()) # list of statements
            return custom_ast.BlockNode(stmts_in_block, line_no=self.get_line_number(ctx.LBRACE()))
        return None # Should ideally not be reached if grammar is complete for statements

    # variableDeclaration: typeSpecifier ID (ASSIGN expression)?;
    def visitVariableDeclaration(self, ctx:MiniCParser.VariableDeclarationContext):
        var_type_node = self.visit(ctx.typeSpecifier())
        var_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        initializer_node = None
        if ctx.ASSIGN() and ctx.expression(): # Check if ASSIGN and expression exist
            initializer_node = self.visit(ctx.expression())
        return custom_ast.VarDeclNode(var_type_node, var_name_node, initializer_node, line_no=self.get_line_number(ctx))

    # ifStatement: IF LPAREN expression RPAREN statement (ELSE statement)?;
    def visitIfStatement(self, ctx:MiniCParser.IfStatementContext):
        condition_node = self.visit(ctx.expression())
        # ANTLR creates a list for statement if there's an ELSE
        then_stmt_node = self.visit(ctx.statement(0))
        else_stmt_node = None
        if ctx.ELSE():
            if len(ctx.statement()) > 1: # Make sure there's a second statement for else
                else_stmt_node = self.visit(ctx.statement(1))
        return custom_ast.IfNode(condition_node, then_stmt_node, else_stmt_node, line_no=self.get_line_number(ctx))

    # whileStatement: WHILE LPAREN expression RPAREN statement;
    def visitWhileStatement(self, ctx:MiniCParser.WhileStatementContext):
        condition_node = self.visit(ctx.expression())
        body_stmt_node = self.visit(ctx.statement())
        return custom_ast.WhileNode(condition_node, body_stmt_node, line_no=self.get_line_number(ctx))

    # forStatement: FOR LPAREN forInitializer? SEMICOLON expression? SEMICOLON expression? RPAREN statement;
    def visitForStatement(self, ctx:MiniCParser.ForStatementContext):
        init_node = None
        if ctx.forInitializer():
            init_node = self.visit(ctx.forInitializer())
        
        # ANTLR's ctx.expression() returns a list of all expression contexts in this rule
        expr_contexts = ctx.expression() # This will be a list
        condition_node = None
        update_node = None

        if len(expr_contexts) == 1: # Only one expression present
            if ctx.forInitializer() or (not ctx.forInitializer() and ctx.getChild(3) == ctx.SEMICOLON(0)):
                # If init present OR (no init AND first semicolon is present before this expr)
                # -> this is the condition
                 condition_node = self.visit(expr_contexts[0])
            else: # No init, and first semicolon missing before it -> this is the update
                 update_node = self.visit(expr_contexts[0])

        elif len(expr_contexts) == 2: # Both condition and update are present
            condition_node = self.visit(expr_contexts[0])
            update_node = self.visit(expr_contexts[1])
            
        body_stmt_node = self.visit(ctx.statement())
        return custom_ast.ForNode(init_node, condition_node, update_node, body_stmt_node, line_no=self.get_line_number(ctx))

    # forInitializer: variableDeclaration | expression;
    def visitForInitializer(self, ctx:MiniCParser.ForInitializerContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None

    # returnStatement: RETURN expression?;
    def visitReturnStatement(self, ctx:MiniCParser.ReturnStatementContext):
        expr_node = None
        if ctx.expression():
            expr_node = self.visit(ctx.expression())
        return custom_ast.ReturnNode(expr_node, line_no=self.get_line_number(ctx))

    # expression: assignmentExpression;
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visit(ctx.assignmentExpression())

    # assignmentExpression: logicalOrExpression (ASSIGN expression)?;
    def visitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        # The rule means: an assignmentExpression IS a logicalOrExpression,
        # OR it's a logicalOrExpression ASSIGN expression.
        left_expr = self.visit(ctx.logicalOrExpression()) # This is always present

        if ctx.ASSIGN(): # It's an assignment
            # We need to ensure the left_expr is a valid lvalue (IdentifierNode for MiniC)
            # For now, we assume the input MiniC is semantically valid for assignments.
            # If left_expr is not an IdentifierNode, our AST structure might be violated
            # or the obfuscator/generator might fail.
            if not isinstance(left_expr, custom_ast.IdentifierNode):
                print(f"Warning: Line {self.get_line_number(ctx)}: LHS of assignment is not a simple Identifier. AST structure for AssignmentNode might be problematic.")
                # Potentially raise an error or return a different node type if MiniC allowed complex lvalues.
            
            rvalue_node = self.visit(ctx.expression()) # The expression on the RHS of ASSIGN
            return custom_ast.AssignmentNode(left_expr, rvalue_node, line_no=self.get_line_number(ctx.ASSIGN()))
        else:
            # Not an assignment, just the logicalOrExpression itself
            return left_expr

    def _build_binary_expression_tree(self, expr_contexts, op_terminals_list, line_ctx):
        # Helper to build left-associative binary trees from ANTLR context lists
        # expr_contexts: list of operand contexts (e.g., ctx.logicalAndExpression())
        # op_terminals_list: list of operator terminal nodes (e.g., ctx.OR())
        
        left_operand = self.visit(expr_contexts[0])
        
        for i in range(len(op_terminals_list)):
            op_token = op_terminals_list[i]
            op_symbol = op_token.getText()
            line_num = self.get_line_number(op_token)
            
            right_operand = self.visit(expr_contexts[i+1])
            left_operand = custom_ast.BinaryOpNode(left_operand, op_symbol, right_operand, line_no=line_num)
            
        return left_operand

    def visitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        return self._build_binary_expression_tree(ctx.logicalAndExpression(), ctx.OR(), ctx)
        
    def visitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        return self._build_binary_expression_tree(ctx.equalityExpression(), ctx.AND(), ctx)

    def visitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        # Handles mixed operators like EQ | NE
        left = self.visit(ctx.relationalExpression(0))
        # Loop through operators if any
        for i in range(len(ctx.relationalExpression()) - 1):
            op_node = ctx.getChild(i * 2 + 1) # Gets the operator token node
            op_symbol = op_node.getText()
            line_num = self.get_line_number(op_node)
            right = self.visit(ctx.relationalExpression(i + 1))
            left = custom_ast.BinaryOpNode(left, op_symbol, right, line_no=line_num)
        return left

    def visitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        # Handles mixed operators like LT | LE | GT | GE
        left = self.visit(ctx.additiveExpression(0))
        for i in range(len(ctx.additiveExpression()) - 1):
            op_node = ctx.getChild(i * 2 + 1)
            op_symbol = op_node.getText()
            line_num = self.get_line_number(op_node)
            right = self.visit(ctx.additiveExpression(i + 1))
            left = custom_ast.BinaryOpNode(left, op_symbol, right, line_no=line_num)
        return left

    def visitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        # Collect all PLUS and MINUS tokens to maintain order
        operators = []
        children = list(ctx.getChildren())
        for child in children:
            if isinstance(child, tree.Tree.TerminalNodeImpl):
                if child.symbol.type == MiniCParser.PLUS or child.symbol.type == MiniCParser.MINUS:
                    operators.append(child)
        return self._build_binary_expression_tree(ctx.multiplicativeExpression(), operators, ctx)

    def visitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        operators = []
        children = list(ctx.getChildren())
        for child in children:
            if isinstance(child, tree.Tree.TerminalNodeImpl):
                if child.symbol.type in [MiniCParser.TIMES, MiniCParser.DIVIDE, MiniCParser.MODULO]:
                    operators.append(child)
        return self._build_binary_expression_tree(ctx.unaryExpression(), operators, ctx)


    # unaryExpression: (PLUS | MINUS | NOT) unaryExpression | primaryExpression;
    def visitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        if ctx.primaryExpression():
            return self.visit(ctx.primaryExpression())
        else:
            op_symbol_node = ctx.getChild(0) # The operator token
            op_symbol = op_symbol_node.getText()
            line_num = self.get_line_number(op_symbol_node)
            
            expr_node = self.visit(ctx.unaryExpression()) # Operand
            return custom_ast.UnaryOpNode(op_symbol, expr_node, line_no=line_num)

    # primaryExpression: LPAREN expression RPAREN | ID | literal | functionCall;
    def visitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        if ctx.LPAREN():
            return self.visit(ctx.expression())
        elif ctx.ID():
            return custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        return None

    # functionCall: ID LPAREN argumentList? RPAREN;
    def visitFunctionCall(self, ctx:MiniCParser.FunctionCallContext):
        func_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        arg_nodes = []
        if ctx.argumentList():
            arg_nodes = self.visit(ctx.argumentList()) # visitArgumentList returns a list
        return custom_ast.FunctionCallNode(func_name_node, arg_nodes, line_no=self.get_line_number(ctx))

    # argumentList: expression (COMMA expression)*;
    def visitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        args = []
        for expr_ctx in ctx.expression():
            args.append(self.visit(expr_ctx))
        return args # Returns a list of ExpressionNode

    # literal: NUMBER | CHAR_LITERAL | STRING_LITERAL | TRUE | FALSE;
    def visitLiteral(self, ctx:MiniCParser.LiteralContext):
        line_num = self.get_line_number(ctx.getChild(0)) # Get line from the token itself
        if ctx.NUMBER():
            return custom_ast.NumberLiteralNode(int(ctx.NUMBER().getText()), line_no=line_num)
        elif ctx.CHAR_LITERAL():
            text = ctx.CHAR_LITERAL().getText()
            val_str = text[1:-1] # Remove outer quotes
            # Unescape common sequences for char
            if val_str == '\\n': val = '\n'
            elif val_str == '\\t': val = '\t'
            elif val_str == '\\r': val = '\r'
            elif val_str == "\\'": val = "'"
            elif val_str == '\\\\': val = '\\'
            else: val = val_str # Single character
            return custom_ast.CharLiteralNode(val, line_no=line_num)
        elif ctx.STRING_LITERAL():
            text = ctx.STRING_LITERAL().getText()
            # Remove quotes and perform basic unescaping for string
            # More robust unescaping might be needed for all C escapes
            val_str = text[1:-1]
            try: # Use Python's string escape handling if possible, but be careful
                # This might be too broad or not perfectly C-compliant
                # A simpler approach for MiniC might be manual replacement:
                val = val_str.replace('\\n', '\n').replace('\\t', '\t').replace('\\r', '\r') \
                             .replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
            except ValueError: # Fallback if complex escapes are not handled by simple replaces
                val = val_str 
            return custom_ast.StringLiteralNode(val, line_no=line_num)
        elif ctx.TRUE():
            return custom_ast.BoolLiteralNode(True, line_no=line_num)
        elif ctx.FALSE():
            return custom_ast.BoolLiteralNode(False, line_no=line_num)
        return None