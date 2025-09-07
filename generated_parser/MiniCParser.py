# Generated from MiniC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,288,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,4,0,64,8,0,11,0,12,0,
        65,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,76,8,2,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,4,1,4,1,4,5,4,88,8,4,10,4,12,4,91,9,4,1,5,1,5,1,5,1,
        6,5,6,97,8,6,10,6,12,6,100,9,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,124,8,
        8,1,9,1,9,1,9,1,9,3,9,130,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        3,10,139,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,3,12,
        150,8,12,1,12,1,12,3,12,154,8,12,1,12,1,12,3,12,158,8,12,1,12,1,
        12,1,12,1,13,1,13,3,13,165,8,13,1,14,1,14,3,14,169,8,14,1,15,1,15,
        1,15,1,15,1,15,1,15,5,15,177,8,15,10,15,12,15,180,9,15,1,15,3,15,
        183,8,15,1,15,1,15,1,16,1,16,1,16,1,16,4,16,191,8,16,11,16,12,16,
        192,1,17,1,17,1,17,4,17,198,8,17,11,17,12,17,199,1,18,1,18,1,19,
        1,19,1,19,3,19,207,8,19,1,20,1,20,1,20,5,20,212,8,20,10,20,12,20,
        215,9,20,1,21,1,21,1,21,5,21,220,8,21,10,21,12,21,223,9,21,1,22,
        1,22,1,22,5,22,228,8,22,10,22,12,22,231,9,22,1,23,1,23,1,23,5,23,
        236,8,23,10,23,12,23,239,9,23,1,24,1,24,1,24,5,24,244,8,24,10,24,
        12,24,247,9,24,1,25,1,25,1,25,5,25,252,8,25,10,25,12,25,255,9,25,
        1,26,1,26,1,26,3,26,260,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        3,27,269,8,27,1,28,1,28,1,28,3,28,274,8,28,1,28,1,28,1,29,1,29,1,
        29,5,29,281,8,29,10,29,12,29,284,9,29,1,30,1,30,1,30,0,0,31,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,0,7,1,0,1,3,1,0,31,32,1,0,27,30,1,0,36,37,1,0,
        38,40,1,0,35,37,2,0,9,10,16,18,292,0,63,1,0,0,0,2,69,1,0,0,0,4,71,
        1,0,0,0,6,82,1,0,0,0,8,84,1,0,0,0,10,92,1,0,0,0,12,98,1,0,0,0,14,
        101,1,0,0,0,16,123,1,0,0,0,18,125,1,0,0,0,20,131,1,0,0,0,22,140,
        1,0,0,0,24,146,1,0,0,0,26,164,1,0,0,0,28,166,1,0,0,0,30,170,1,0,
        0,0,32,186,1,0,0,0,34,194,1,0,0,0,36,201,1,0,0,0,38,203,1,0,0,0,
        40,208,1,0,0,0,42,216,1,0,0,0,44,224,1,0,0,0,46,232,1,0,0,0,48,240,
        1,0,0,0,50,248,1,0,0,0,52,259,1,0,0,0,54,268,1,0,0,0,56,270,1,0,
        0,0,58,277,1,0,0,0,60,285,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,
        65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,5,0,0,
        1,68,1,1,0,0,0,69,70,3,4,2,0,70,3,1,0,0,0,71,72,3,6,3,0,72,73,5,
        15,0,0,73,75,5,19,0,0,74,76,3,8,4,0,75,74,1,0,0,0,75,76,1,0,0,0,
        76,77,1,0,0,0,77,78,5,20,0,0,78,79,5,21,0,0,79,80,3,12,6,0,80,81,
        5,22,0,0,81,5,1,0,0,0,82,83,7,0,0,0,83,7,1,0,0,0,84,89,3,10,5,0,
        85,86,5,24,0,0,86,88,3,10,5,0,87,85,1,0,0,0,88,91,1,0,0,0,89,87,
        1,0,0,0,89,90,1,0,0,0,90,9,1,0,0,0,91,89,1,0,0,0,92,93,3,6,3,0,93,
        94,5,15,0,0,94,11,1,0,0,0,95,97,3,16,8,0,96,95,1,0,0,0,97,100,1,
        0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,13,1,0,0,0,100,98,1,0,0,0,101,
        102,5,14,0,0,102,103,5,23,0,0,103,15,1,0,0,0,104,105,3,18,9,0,105,
        106,5,23,0,0,106,124,1,0,0,0,107,108,3,36,18,0,108,109,5,23,0,0,
        109,124,1,0,0,0,110,124,3,20,10,0,111,124,3,22,11,0,112,124,3,24,
        12,0,113,114,3,28,14,0,114,115,5,23,0,0,115,124,1,0,0,0,116,117,
        5,21,0,0,117,118,3,12,6,0,118,119,5,22,0,0,119,124,1,0,0,0,120,124,
        3,30,15,0,121,122,5,14,0,0,122,124,5,23,0,0,123,104,1,0,0,0,123,
        107,1,0,0,0,123,110,1,0,0,0,123,111,1,0,0,0,123,112,1,0,0,0,123,
        113,1,0,0,0,123,116,1,0,0,0,123,120,1,0,0,0,123,121,1,0,0,0,124,
        17,1,0,0,0,125,126,3,6,3,0,126,129,5,15,0,0,127,128,5,26,0,0,128,
        130,3,36,18,0,129,127,1,0,0,0,129,130,1,0,0,0,130,19,1,0,0,0,131,
        132,5,4,0,0,132,133,5,19,0,0,133,134,3,36,18,0,134,135,5,20,0,0,
        135,138,3,16,8,0,136,137,5,5,0,0,137,139,3,16,8,0,138,136,1,0,0,
        0,138,139,1,0,0,0,139,21,1,0,0,0,140,141,5,6,0,0,141,142,5,19,0,
        0,142,143,3,36,18,0,143,144,5,20,0,0,144,145,3,16,8,0,145,23,1,0,
        0,0,146,147,5,7,0,0,147,149,5,19,0,0,148,150,3,26,13,0,149,148,1,
        0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,153,5,23,0,0,152,154,3,
        36,18,0,153,152,1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,157,
        5,23,0,0,156,158,3,36,18,0,157,156,1,0,0,0,157,158,1,0,0,0,158,159,
        1,0,0,0,159,160,5,20,0,0,160,161,3,16,8,0,161,25,1,0,0,0,162,165,
        3,18,9,0,163,165,3,36,18,0,164,162,1,0,0,0,164,163,1,0,0,0,165,27,
        1,0,0,0,166,168,5,8,0,0,167,169,3,36,18,0,168,167,1,0,0,0,168,169,
        1,0,0,0,169,29,1,0,0,0,170,171,5,11,0,0,171,172,5,19,0,0,172,173,
        3,36,18,0,173,174,5,20,0,0,174,178,5,21,0,0,175,177,3,32,16,0,176,
        175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        182,1,0,0,0,180,178,1,0,0,0,181,183,3,34,17,0,182,181,1,0,0,0,182,
        183,1,0,0,0,183,184,1,0,0,0,184,185,5,22,0,0,185,31,1,0,0,0,186,
        187,5,12,0,0,187,188,3,60,30,0,188,190,5,25,0,0,189,191,3,16,8,0,
        190,189,1,0,0,0,191,192,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,
        193,33,1,0,0,0,194,195,5,13,0,0,195,197,5,25,0,0,196,198,3,16,8,
        0,197,196,1,0,0,0,198,199,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,
        0,200,35,1,0,0,0,201,202,3,38,19,0,202,37,1,0,0,0,203,206,3,40,20,
        0,204,205,5,26,0,0,205,207,3,36,18,0,206,204,1,0,0,0,206,207,1,0,
        0,0,207,39,1,0,0,0,208,213,3,42,21,0,209,210,5,34,0,0,210,212,3,
        42,21,0,211,209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,
        1,0,0,0,214,41,1,0,0,0,215,213,1,0,0,0,216,221,3,44,22,0,217,218,
        5,33,0,0,218,220,3,44,22,0,219,217,1,0,0,0,220,223,1,0,0,0,221,219,
        1,0,0,0,221,222,1,0,0,0,222,43,1,0,0,0,223,221,1,0,0,0,224,229,3,
        46,23,0,225,226,7,1,0,0,226,228,3,46,23,0,227,225,1,0,0,0,228,231,
        1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,45,1,0,0,0,231,229,1,
        0,0,0,232,237,3,48,24,0,233,234,7,2,0,0,234,236,3,48,24,0,235,233,
        1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,47,1,
        0,0,0,239,237,1,0,0,0,240,245,3,50,25,0,241,242,7,3,0,0,242,244,
        3,50,25,0,243,241,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,
        1,0,0,0,246,49,1,0,0,0,247,245,1,0,0,0,248,253,3,52,26,0,249,250,
        7,4,0,0,250,252,3,52,26,0,251,249,1,0,0,0,252,255,1,0,0,0,253,251,
        1,0,0,0,253,254,1,0,0,0,254,51,1,0,0,0,255,253,1,0,0,0,256,257,7,
        5,0,0,257,260,3,52,26,0,258,260,3,54,27,0,259,256,1,0,0,0,259,258,
        1,0,0,0,260,53,1,0,0,0,261,262,5,19,0,0,262,263,3,36,18,0,263,264,
        5,20,0,0,264,269,1,0,0,0,265,269,5,15,0,0,266,269,3,60,30,0,267,
        269,3,56,28,0,268,261,1,0,0,0,268,265,1,0,0,0,268,266,1,0,0,0,268,
        267,1,0,0,0,269,55,1,0,0,0,270,271,5,15,0,0,271,273,5,19,0,0,272,
        274,3,58,29,0,273,272,1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,
        276,5,20,0,0,276,57,1,0,0,0,277,282,3,36,18,0,278,279,5,24,0,0,279,
        281,3,36,18,0,280,278,1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,
        283,1,0,0,0,283,59,1,0,0,0,284,282,1,0,0,0,285,286,7,6,0,0,286,61,
        1,0,0,0,27,65,75,89,98,123,129,138,149,153,157,164,168,178,182,192,
        199,206,213,221,229,237,245,253,259,268,273,282
    ]

class MiniCParser ( Parser ):

    grammarFileName = "MiniC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'char'", "'bool'", "'if'", "'else'", 
                     "'while'", "'for'", "'return'", "'true'", "'false'", 
                     "'switch'", "'case'", "'default'", "'break'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "';'", "','", "':'", "'='", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'&&'", "'||'", "'!'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "INT", "CHAR", "BOOL", "IF", "ELSE", 
                      "WHILE", "FOR", "RETURN", "TRUE", "FALSE", "SWITCH", 
                      "CASE", "DEFAULT", "BREAK", "ID", "NUMBER", "CHAR_LITERAL", 
                      "STRING_LITERAL", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "SEMICOLON", "COMMA", "COLON", "ASSIGN", "GT", "LT", 
                      "GE", "LE", "EQ", "NE", "AND", "OR", "NOT", "PLUS", 
                      "MINUS", "TIMES", "DIVIDE", "MODULO", "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_functionDefinition = 2
    RULE_typeSpecifier = 3
    RULE_parameters = 4
    RULE_parameter = 5
    RULE_blockContent = 6
    RULE_breakStatement = 7
    RULE_statement = 8
    RULE_variableDeclaration = 9
    RULE_ifStatement = 10
    RULE_whileStatement = 11
    RULE_forStatement = 12
    RULE_forInitializer = 13
    RULE_returnStatement = 14
    RULE_switchStatement = 15
    RULE_caseStatement = 16
    RULE_defaultStatement = 17
    RULE_expression = 18
    RULE_assignmentExpression = 19
    RULE_logicalOrExpression = 20
    RULE_logicalAndExpression = 21
    RULE_equalityExpression = 22
    RULE_relationalExpression = 23
    RULE_additiveExpression = 24
    RULE_multiplicativeExpression = 25
    RULE_unaryExpression = 26
    RULE_primaryExpression = 27
    RULE_functionCall = 28
    RULE_argumentList = 29
    RULE_literal = 30

    ruleNames =  [ "program", "declaration", "functionDefinition", "typeSpecifier", 
                   "parameters", "parameter", "blockContent", "breakStatement", 
                   "statement", "variableDeclaration", "ifStatement", "whileStatement", 
                   "forStatement", "forInitializer", "returnStatement", 
                   "switchStatement", "caseStatement", "defaultStatement", 
                   "expression", "assignmentExpression", "logicalOrExpression", 
                   "logicalAndExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "primaryExpression", "functionCall", "argumentList", 
                   "literal" ]

    EOF = Token.EOF
    INT=1
    CHAR=2
    BOOL=3
    IF=4
    ELSE=5
    WHILE=6
    FOR=7
    RETURN=8
    TRUE=9
    FALSE=10
    SWITCH=11
    CASE=12
    DEFAULT=13
    BREAK=14
    ID=15
    NUMBER=16
    CHAR_LITERAL=17
    STRING_LITERAL=18
    LPAREN=19
    RPAREN=20
    LBRACE=21
    RBRACE=22
    SEMICOLON=23
    COMMA=24
    COLON=25
    ASSIGN=26
    GT=27
    LT=28
    GE=29
    LE=30
    EQ=31
    NE=32
    AND=33
    OR=34
    NOT=35
    PLUS=36
    MINUS=37
    TIMES=38
    DIVIDE=39
    MODULO=40
    WS=41
    LINE_COMMENT=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniCParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniCParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.declaration()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    break

            self.state = 67
            self.match(MiniCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self):
            return self.getTypedRuleContext(MiniCParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.functionDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniCParser.LBRACE, 0)

        def blockContent(self):
            return self.getTypedRuleContext(MiniCParser.BlockContentContext,0)


        def RBRACE(self):
            return self.getToken(MiniCParser.RBRACE, 0)

        def parameters(self):
            return self.getTypedRuleContext(MiniCParser.ParametersContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = MiniCParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.typeSpecifier()
            self.state = 72
            self.match(MiniCParser.ID)
            self.state = 73
            self.match(MiniCParser.LPAREN)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 74
                self.parameters()


            self.state = 77
            self.match(MiniCParser.RPAREN)
            self.state = 78
            self.match(MiniCParser.LBRACE)
            self.state = 79
            self.blockContent()
            self.state = 80
            self.match(MiniCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniCParser.INT, 0)

        def CHAR(self):
            return self.getToken(MiniCParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(MiniCParser.BOOL, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = MiniCParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.COMMA)
            else:
                return self.getToken(MiniCParser.COMMA, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MiniCParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.parameter()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 85
                self.match(MiniCParser.COMMA)
                self.state = 86
                self.parameter()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.typeSpecifier()
            self.state = 93
            self.match(MiniCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_blockContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockContent" ):
                listener.enterBlockContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockContent" ):
                listener.exitBlockContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockContent" ):
                return visitor.visitBlockContent(self)
            else:
                return visitor.visitChildren(self)




    def blockContent(self):

        localctx = MiniCParser.BlockContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_blockContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 240521301982) != 0):
                self.state = 95
                self.statement()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniCParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniCParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MiniCParser.BREAK)
            self.state = 102
            self.match(MiniCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniCParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniCParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniCParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MiniCParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniCParser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniCParser.ReturnStatementContext,0)


        def LBRACE(self):
            return self.getToken(MiniCParser.LBRACE, 0)

        def blockContent(self):
            return self.getTypedRuleContext(MiniCParser.BlockContentContext,0)


        def RBRACE(self):
            return self.getToken(MiniCParser.RBRACE, 0)

        def switchStatement(self):
            return self.getTypedRuleContext(MiniCParser.SwitchStatementContext,0)


        def BREAK(self):
            return self.getToken(MiniCParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.variableDeclaration()
                self.state = 105
                self.match(MiniCParser.SEMICOLON)
                pass
            elif token in [9, 10, 15, 16, 17, 18, 19, 35, 36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.expression()
                self.state = 108
                self.match(MiniCParser.SEMICOLON)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.ifStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.whileStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.forStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.returnStatement()
                self.state = 114
                self.match(MiniCParser.SEMICOLON)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 7)
                self.state = 116
                self.match(MiniCParser.LBRACE)
                self.state = 117
                self.blockContent()
                self.state = 118
                self.match(MiniCParser.RBRACE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 120
                self.switchStatement()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 9)
                self.state = 121
                self.match(MiniCParser.BREAK)
                self.state = 122
                self.match(MiniCParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(MiniCParser.TypeSpecifierContext,0)


        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = MiniCParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.typeSpecifier()
            self.state = 126
            self.match(MiniCParser.ID)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 127
                self.match(MiniCParser.ASSIGN)
                self.state = 128
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniCParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MiniCParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniCParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MiniCParser.IF)
            self.state = 132
            self.match(MiniCParser.LPAREN)
            self.state = 133
            self.expression()
            self.state = 134
            self.match(MiniCParser.RPAREN)
            self.state = 135
            self.statement()
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 136
                self.match(MiniCParser.ELSE)
                self.state = 137
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniCParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniCParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MiniCParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(MiniCParser.WHILE)
            self.state = 141
            self.match(MiniCParser.LPAREN)
            self.state = 142
            self.expression()
            self.state = 143
            self.match(MiniCParser.RPAREN)
            self.state = 144
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniCParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.SEMICOLON)
            else:
                return self.getToken(MiniCParser.SEMICOLON, i)

        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniCParser.StatementContext,0)


        def forInitializer(self):
            return self.getTypedRuleContext(MiniCParser.ForInitializerContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniCParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MiniCParser.FOR)
            self.state = 147
            self.match(MiniCParser.LPAREN)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240519185934) != 0):
                self.state = 148
                self.forInitializer()


            self.state = 151
            self.match(MiniCParser.SEMICOLON)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240519185920) != 0):
                self.state = 152
                self.expression()


            self.state = 155
            self.match(MiniCParser.SEMICOLON)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240519185920) != 0):
                self.state = 156
                self.expression()


            self.state = 159
            self.match(MiniCParser.RPAREN)
            self.state = 160
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MiniCParser.VariableDeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_forInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitializer" ):
                listener.enterForInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitializer" ):
                listener.exitForInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitializer" ):
                return visitor.visitForInitializer(self)
            else:
                return visitor.visitChildren(self)




    def forInitializer(self):

        localctx = MiniCParser.ForInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forInitializer)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.variableDeclaration()
                pass
            elif token in [9, 10, 15, 16, 17, 18, 19, 35, 36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniCParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniCParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniCParser.RETURN)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240519185920) != 0):
                self.state = 167
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(MiniCParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniCParser.RBRACE, 0)

        def caseStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.CaseStatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.CaseStatementContext,i)


        def defaultStatement(self):
            return self.getTypedRuleContext(MiniCParser.DefaultStatementContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = MiniCParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MiniCParser.SWITCH)
            self.state = 171
            self.match(MiniCParser.LPAREN)
            self.state = 172
            self.expression()
            self.state = 173
            self.match(MiniCParser.RPAREN)
            self.state = 174
            self.match(MiniCParser.LBRACE)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 175
                self.caseStatement()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 181
                self.defaultStatement()


            self.state = 184
            self.match(MiniCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(MiniCParser.CASE, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniCParser.LiteralContext,0)


        def COLON(self):
            return self.getToken(MiniCParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_caseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStatement" ):
                listener.enterCaseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStatement" ):
                listener.exitCaseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStatement" ):
                return visitor.visitCaseStatement(self)
            else:
                return visitor.visitChildren(self)




    def caseStatement(self):

        localctx = MiniCParser.CaseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_caseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(MiniCParser.CASE)
            self.state = 187
            self.literal()
            self.state = 188
            self.match(MiniCParser.COLON)
            self.state = 190 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 189
                self.statement()
                self.state = 192 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 240521301982) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(MiniCParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(MiniCParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_defaultStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultStatement" ):
                listener.enterDefaultStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultStatement" ):
                listener.exitDefaultStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultStatement" ):
                return visitor.visitDefaultStatement(self)
            else:
                return visitor.visitChildren(self)




    def defaultStatement(self):

        localctx = MiniCParser.DefaultStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_defaultStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MiniCParser.DEFAULT)
            self.state = 195
            self.match(MiniCParser.COLON)
            self.state = 197 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 196
                self.statement()
                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 240521301982) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(MiniCParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(MiniCParser.LogicalOrExpressionContext,0)


        def ASSIGN(self):
            return self.getToken(MiniCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = MiniCParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignmentExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.logicalOrExpression()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 204
                self.match(MiniCParser.ASSIGN)
                self.state = 205
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.OR)
            else:
                return self.getToken(MiniCParser.OR, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = MiniCParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.logicalAndExpression()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 209
                self.match(MiniCParser.OR)
                self.state = 210
                self.logicalAndExpression()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.AND)
            else:
                return self.getToken(MiniCParser.AND, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = MiniCParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.equalityExpression()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 217
                self.match(MiniCParser.AND)
                self.state = 218
                self.equalityExpression()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.RelationalExpressionContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.EQ)
            else:
                return self.getToken(MiniCParser.EQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.NE)
            else:
                return self.getToken(MiniCParser.NE, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = MiniCParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.relationalExpression()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.relationalExpression()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.AdditiveExpressionContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.LT)
            else:
                return self.getToken(MiniCParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.LE)
            else:
                return self.getToken(MiniCParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.GT)
            else:
                return self.getToken(MiniCParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.GE)
            else:
                return self.getToken(MiniCParser.GE, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = MiniCParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.additiveExpression()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0):
                self.state = 233
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 234
                self.additiveExpression()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.PLUS)
            else:
                return self.getToken(MiniCParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.MINUS)
            else:
                return self.getToken(MiniCParser.MINUS, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = MiniCParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.multiplicativeExpression()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36 or _la==37:
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==36 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.multiplicativeExpression()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.UnaryExpressionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.TIMES)
            else:
                return self.getToken(MiniCParser.TIMES, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.DIVIDE)
            else:
                return self.getToken(MiniCParser.DIVIDE, i)

        def MODULO(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.MODULO)
            else:
                return self.getToken(MiniCParser.MODULO, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = MiniCParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.unaryExpression()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0):
                self.state = 249
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.unaryExpression()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(MiniCParser.UnaryExpressionContext,0)


        def PLUS(self):
            return self.getToken(MiniCParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniCParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniCParser.NOT, 0)

        def primaryExpression(self):
            return self.getTypedRuleContext(MiniCParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = MiniCParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168576) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.unaryExpression()
                pass
            elif token in [9, 10, 15, 16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniCParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MiniCParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = MiniCParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primaryExpression)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(MiniCParser.LPAREN)
                self.state = 262
                self.expression()
                self.state = 263
                self.match(MiniCParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(MiniCParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 267
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniCParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniCParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MiniCParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MiniCParser.ID)
            self.state = 271
            self.match(MiniCParser.LPAREN)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240519185920) != 0):
                self.state = 272
                self.argumentList()


            self.state = 275
            self.match(MiniCParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.COMMA)
            else:
                return self.getToken(MiniCParser.COMMA, i)

        def getRuleIndex(self):
            return MiniCParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = MiniCParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.expression()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 278
                self.match(MiniCParser.COMMA)
                self.state = 279
                self.expression()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MiniCParser.NUMBER, 0)

        def CHAR_LITERAL(self):
            return self.getToken(MiniCParser.CHAR_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniCParser.STRING_LITERAL, 0)

        def TRUE(self):
            return self.getToken(MiniCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniCParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 460288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





