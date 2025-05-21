from antlr4 import *

if __name__ is not None and "." in __name__:

    from .generated_parser.MiniCParser import MiniCParser
    from .generated_parser.MiniCVisitor import MiniCVisitor
else:

    from generated_parser.MiniCParser import MiniCParser
    from generated_parser.MiniCVisitor import MiniCVisitor

import ast_nodes as custom_ast


class ASTBuilderVisitor(MiniCVisitor):

    def get_line_number(self, ctx_or_token):
        if hasattr(ctx_or_token, 'start'):
            return ctx_or_token.start.line
        elif hasattr(ctx_or_token, 'symbol'):
            return ctx_or_token.symbol.line
        elif hasattr(ctx_or_token, 'line'):
            return ctx_or_token.line
        return -1

    def visitProgram(self, ctx: MiniCParser.ProgramContext):
        declarations = []
        for decl_ctx in ctx.declaration():
            declarations.append(self.visit(decl_ctx))
        declarations = [d for d in declarations if d is not None]
        return custom_ast.ProgramNode(declarations, line_no=self.get_line_number(ctx))

    def visitDeclaration(self, ctx: MiniCParser.DeclarationContext):
        if ctx.functionDefinition():
            return self.visit(ctx.functionDefinition())
        return None

    def visitFunctionDefinition(self, ctx: MiniCParser.FunctionDefinitionContext):
        return_type_node = self.visit(ctx.typeSpecifier())
        func_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))

        param_nodes = []
        if ctx.parameters():
            param_nodes = self.visit(ctx.parameters())

        body_stmts_list = self.visit(ctx.blockContent())
        body_block_node = custom_ast.BlockNode(body_stmts_list, line_no=self.get_line_number(ctx.LBRACE()))

        return custom_ast.FunctionDefNode(return_type_node, func_name_node, param_nodes, body_block_node,
                                          line_no=self.get_line_number(ctx))

    def visitTypeSpecifier(self, ctx: MiniCParser.TypeSpecifierContext):
        type_name = ctx.getText()
        return custom_ast.TypeNode(type_name, line_no=self.get_line_number(ctx))

    def visitParameters(self, ctx: MiniCParser.ParametersContext):
        params = []
        for param_ctx in ctx.parameter():
            params.append(self.visit(param_ctx))
        return params

    def visitParameter(self, ctx: MiniCParser.ParameterContext):
        param_type_node = self.visit(ctx.typeSpecifier())
        param_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        return custom_ast.ParamNode(param_type_node, param_name_node, line_no=self.get_line_number(ctx))

    def visitBlockContent(self, ctx: MiniCParser.BlockContentContext):
        statements = []
        for stmt_ctx in ctx.statement():
            statements.append(self.visit(stmt_ctx))
        return statements

    def visitStatement(self, ctx: MiniCParser.StatementContext):
        if ctx.variableDeclaration():

            return self.visit(ctx.variableDeclaration())
        elif ctx.expression():
            expr_node = self.visit(ctx.expression())
            return custom_ast.ExprStatementNode(expr_node, line_no=self.get_line_number(ctx))
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.LBRACE() and ctx.blockContent() and ctx.RBRACE():
            stmts_in_block = self.visit(ctx.blockContent())
            return custom_ast.BlockNode(stmts_in_block, line_no=self.get_line_number(ctx.LBRACE()))
        return None

    def visitVariableDeclaration(self, ctx: MiniCParser.VariableDeclarationContext):
        var_type_node = self.visit(ctx.typeSpecifier())
        var_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        initializer_node = None
        if ctx.ASSIGN() and ctx.expression():
            initializer_node = self.visit(ctx.expression())
        return custom_ast.VarDeclNode(var_type_node, var_name_node, initializer_node, line_no=self.get_line_number(ctx))

    def visitIfStatement(self, ctx: MiniCParser.IfStatementContext):
        condition_node = self.visit(ctx.expression())
        then_stmt_node = self.visit(ctx.statement(0))
        else_stmt_node = None
        if ctx.ELSE():
            if len(ctx.statement()) > 1:
                else_stmt_node = self.visit(ctx.statement(1))
        return custom_ast.IfNode(condition_node, then_stmt_node, else_stmt_node, line_no=self.get_line_number(ctx))

    def visitWhileStatement(self, ctx: MiniCParser.WhileStatementContext):
        condition_node = self.visit(ctx.expression())
        body_stmt_node = self.visit(ctx.statement())
        return custom_ast.WhileNode(condition_node, body_stmt_node, line_no=self.get_line_number(ctx))

    def visitForStatement(self, ctx: MiniCParser.ForStatementContext):
        init_node = None
        if ctx.forInitializer():
            init_node = self.visit(ctx.forInitializer())

        expr_contexts = ctx.expression()
        condition_node = None
        update_node = None

        if len(expr_contexts) == 1:
            if ctx.forInitializer() or (not ctx.forInitializer() and ctx.getChild(3) == ctx.SEMICOLON(0)):

                condition_node = self.visit(expr_contexts[0])
            else:
                update_node = self.visit(expr_contexts[0])

        elif len(expr_contexts) == 2:
            condition_node = self.visit(expr_contexts[0])
            update_node = self.visit(expr_contexts[1])

        body_stmt_node = self.visit(ctx.statement())
        return custom_ast.ForNode(init_node, condition_node, update_node, body_stmt_node,
                                  line_no=self.get_line_number(ctx))

    def visitForInitializer(self, ctx: MiniCParser.ForInitializerContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None

    def visitReturnStatement(self, ctx: MiniCParser.ReturnStatementContext):
        expr_node = None
        if ctx.expression():
            expr_node = self.visit(ctx.expression())
        return custom_ast.ReturnNode(expr_node, line_no=self.get_line_number(ctx))

    def visitExpression(self, ctx: MiniCParser.ExpressionContext):
        return self.visit(ctx.assignmentExpression())

    def visitAssignmentExpression(self, ctx: MiniCParser.AssignmentExpressionContext):
        left_expr = self.visit(ctx.logicalOrExpression())

        if ctx.ASSIGN():

            if not isinstance(left_expr, custom_ast.IdentifierNode):
                print(
                    f"Warning: Line {self.get_line_number(ctx)}: LHS of assignment is not a simple Identifier. AST "
                    f"structure for AssignmentNode might be problematic.")

            rvalue_node = self.visit(ctx.expression())
            return custom_ast.AssignmentNode(left_expr, rvalue_node, line_no=self.get_line_number(ctx.ASSIGN()))
        else:
            return left_expr

    def _build_binary_expression_tree(self, expr_contexts, op_terminals_list, line_ctx):


        left_operand = self.visit(expr_contexts[0])

        for i in range(len(op_terminals_list)):
            op_token = op_terminals_list[i]
            op_symbol = op_token.getText()
            line_num = self.get_line_number(op_token)

            right_operand = self.visit(expr_contexts[i + 1])
            left_operand = custom_ast.BinaryOpNode(left_operand, op_symbol, right_operand, line_no=line_num)

        return left_operand

    def visitLogicalOrExpression(self, ctx: MiniCParser.LogicalOrExpressionContext):
        return self._build_binary_expression_tree(ctx.logicalAndExpression(), ctx.OR(), ctx)

    def visitLogicalAndExpression(self, ctx: MiniCParser.LogicalAndExpressionContext):
        return self._build_binary_expression_tree(ctx.equalityExpression(), ctx.AND(), ctx)

    def visitEqualityExpression(self, ctx: MiniCParser.EqualityExpressionContext):
        left = self.visit(ctx.relationalExpression(0))
        for i in range(len(ctx.relationalExpression()) - 1):
            op_node = ctx.getChild(i * 2 + 1)
            op_symbol = op_node.getText()
            line_num = self.get_line_number(op_node)
            right = self.visit(ctx.relationalExpression(i + 1))
            left = custom_ast.BinaryOpNode(left, op_symbol, right, line_no=line_num)
        return left

    def visitRelationalExpression(self, ctx: MiniCParser.RelationalExpressionContext):
        left = self.visit(ctx.additiveExpression(0))
        for i in range(len(ctx.additiveExpression()) - 1):
            op_node = ctx.getChild(i * 2 + 1)
            op_symbol = op_node.getText()
            line_num = self.get_line_number(op_node)
            right = self.visit(ctx.additiveExpression(i + 1))
            left = custom_ast.BinaryOpNode(left, op_symbol, right, line_no=line_num)
        return left

    def visitAdditiveExpression(self, ctx: MiniCParser.AdditiveExpressionContext):
        # Collect all PLUS and MINUS tokens to maintain order
        operators = []
        children = list(ctx.getChildren())
        for child in children:
            if isinstance(child, tree.Tree.TerminalNodeImpl):
                if child.symbol.type == MiniCParser.PLUS or child.symbol.type == MiniCParser.MINUS:
                    operators.append(child)
        return self._build_binary_expression_tree(ctx.multiplicativeExpression(), operators, ctx)

    def visitMultiplicativeExpression(self, ctx: MiniCParser.MultiplicativeExpressionContext):
        operators = []
        children = list(ctx.getChildren())
        for child in children:
            if isinstance(child, tree.Tree.TerminalNodeImpl):
                if child.symbol.type in [MiniCParser.TIMES, MiniCParser.DIVIDE, MiniCParser.MODULO]:
                    operators.append(child)
        return self._build_binary_expression_tree(ctx.unaryExpression(), operators, ctx)

    def visitUnaryExpression(self, ctx: MiniCParser.UnaryExpressionContext):
        if ctx.primaryExpression():
            return self.visit(ctx.primaryExpression())
        else:
            op_symbol_node = ctx.getChild(0)
            op_symbol = op_symbol_node.getText()
            line_num = self.get_line_number(op_symbol_node)

            expr_node = self.visit(ctx.unaryExpression())
            return custom_ast.UnaryOpNode(op_symbol, expr_node, line_no=line_num)

    def visitPrimaryExpression(self, ctx: MiniCParser.PrimaryExpressionContext):
        if ctx.LPAREN():
            return self.visit(ctx.expression())
        elif ctx.ID():
            return custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        return None

    def visitFunctionCall(self, ctx: MiniCParser.FunctionCallContext):
        func_name_node = custom_ast.IdentifierNode(ctx.ID().getText(), line_no=self.get_line_number(ctx.ID()))
        arg_nodes = []
        if ctx.argumentList():
            arg_nodes = self.visit(ctx.argumentList())  # visitArgumentList returns a list
        return custom_ast.FunctionCallNode(func_name_node, arg_nodes, line_no=self.get_line_number(ctx))

    def visitArgumentList(self, ctx: MiniCParser.ArgumentListContext):
        args = []
        for expr_ctx in ctx.expression():
            args.append(self.visit(expr_ctx))
        return args

    def visitLiteral(self, ctx: MiniCParser.LiteralContext):
        line_num = self.get_line_number(ctx.getChild(0))
        if ctx.NUMBER():
            return custom_ast.NumberLiteralNode(int(ctx.NUMBER().getText()), line_no=line_num)
        elif ctx.CHAR_LITERAL():
            text = ctx.CHAR_LITERAL().getText()
            val_str = text[1:-1]
            if val_str == '\\n':
                val = '\n'
            elif val_str == '\\t':
                val = '\t'
            elif val_str == '\\r':
                val = '\r'
            elif val_str == "\\'":
                val = "'"
            elif val_str == '\\\\':
                val = '\\'
            else:
                val = val_str
            return custom_ast.CharLiteralNode(val, line_no=line_num)
        elif ctx.STRING_LITERAL():
            text = ctx.STRING_LITERAL().getText()
            val_str = text[1:-1]
            try:
                val = val_str.replace('\\n', '\n').replace('\\t', '\t').replace('\\r', '\r') \
                    .replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
            except ValueError:
                val = val_str
            return custom_ast.StringLiteralNode(val, line_no=line_num)
        elif ctx.TRUE():
            return custom_ast.BoolLiteralNode(True, line_no=line_num)
        elif ctx.FALSE():
            return custom_ast.BoolLiteralNode(False, line_no=line_num)
        return None
