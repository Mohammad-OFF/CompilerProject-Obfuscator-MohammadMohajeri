# Generated from MiniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#declaration.
    def enterDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#declaration.
    def exitDeclaration(self, ctx:MiniCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:MiniCParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by MiniCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:MiniCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameters.
    def enterParameters(self, ctx:MiniCParser.ParametersContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameters.
    def exitParameters(self, ctx:MiniCParser.ParametersContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameter.
    def enterParameter(self, ctx:MiniCParser.ParameterContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameter.
    def exitParameter(self, ctx:MiniCParser.ParameterContext):
        pass


    # Enter a parse tree produced by MiniCParser#blockContent.
    def enterBlockContent(self, ctx:MiniCParser.BlockContentContext):
        pass

    # Exit a parse tree produced by MiniCParser#blockContent.
    def exitBlockContent(self, ctx:MiniCParser.BlockContentContext):
        pass


    # Enter a parse tree produced by MiniCParser#statement.
    def enterStatement(self, ctx:MiniCParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#statement.
    def exitStatement(self, ctx:MiniCParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:MiniCParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:MiniCParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#ifStatement.
    def enterIfStatement(self, ctx:MiniCParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#ifStatement.
    def exitIfStatement(self, ctx:MiniCParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#whileStatement.
    def enterWhileStatement(self, ctx:MiniCParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#whileStatement.
    def exitWhileStatement(self, ctx:MiniCParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#forStatement.
    def enterForStatement(self, ctx:MiniCParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#forStatement.
    def exitForStatement(self, ctx:MiniCParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#forInitializer.
    def enterForInitializer(self, ctx:MiniCParser.ForInitializerContext):
        pass

    # Exit a parse tree produced by MiniCParser#forInitializer.
    def exitForInitializer(self, ctx:MiniCParser.ForInitializerContext):
        pass


    # Enter a parse tree produced by MiniCParser#returnStatement.
    def enterReturnStatement(self, ctx:MiniCParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#returnStatement.
    def exitReturnStatement(self, ctx:MiniCParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#expression.
    def enterExpression(self, ctx:MiniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#expression.
    def exitExpression(self, ctx:MiniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:MiniCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:MiniCParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:MiniCParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:MiniCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:MiniCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MiniCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MiniCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MiniCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:MiniCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#functionCall.
    def enterFunctionCall(self, ctx:MiniCParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MiniCParser#functionCall.
    def exitFunctionCall(self, ctx:MiniCParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MiniCParser#argumentList.
    def enterArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MiniCParser#argumentList.
    def exitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by MiniCParser#literal.
    def enterLiteral(self, ctx:MiniCParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniCParser#literal.
    def exitLiteral(self, ctx:MiniCParser.LiteralContext):
        pass



del MiniCParser