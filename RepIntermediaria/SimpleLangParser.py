# Generated from SimpleLang.g4 by ANTLR 4.13.2
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
        4,1,29,163,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,4,0,39,8,0,11,0,
        12,0,40,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,61,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,70,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,82,8,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,8,1,8,1,9,
        1,9,1,10,1,10,1,10,5,10,105,8,10,10,10,12,10,108,9,10,1,11,1,11,
        1,11,5,11,113,8,11,10,11,12,11,116,9,11,1,12,1,12,1,12,5,12,121,
        8,12,10,12,12,12,124,9,12,1,13,1,13,1,13,5,13,129,8,13,10,13,12,
        13,132,9,13,1,14,1,14,1,14,5,14,137,8,14,10,14,12,14,140,9,14,1,
        15,1,15,1,15,5,15,145,8,15,10,15,12,15,148,9,15,1,16,1,16,1,16,3,
        16,153,8,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,161,8,17,1,17,0,0,
        18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,5,1,0,14,15,
        1,0,16,19,1,0,20,21,1,0,22,23,2,0,21,21,24,24,163,0,38,1,0,0,0,2,
        42,1,0,0,0,4,60,1,0,0,0,6,62,1,0,0,0,8,71,1,0,0,0,10,77,1,0,0,0,
        12,83,1,0,0,0,14,87,1,0,0,0,16,90,1,0,0,0,18,99,1,0,0,0,20,101,1,
        0,0,0,22,109,1,0,0,0,24,117,1,0,0,0,26,125,1,0,0,0,28,133,1,0,0,
        0,30,141,1,0,0,0,32,152,1,0,0,0,34,160,1,0,0,0,36,39,3,2,1,0,37,
        39,3,4,2,0,38,36,1,0,0,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,
        0,40,41,1,0,0,0,41,1,1,0,0,0,42,43,5,1,0,0,43,44,5,25,0,0,44,45,
        5,2,0,0,45,46,5,3,0,0,46,47,3,16,8,0,47,3,1,0,0,0,48,61,3,6,3,0,
        49,61,3,8,4,0,50,51,3,12,6,0,51,52,5,4,0,0,52,61,1,0,0,0,53,54,3,
        10,5,0,54,55,5,4,0,0,55,61,1,0,0,0,56,57,3,14,7,0,57,58,5,4,0,0,
        58,61,1,0,0,0,59,61,5,4,0,0,60,48,1,0,0,0,60,49,1,0,0,0,60,50,1,
        0,0,0,60,53,1,0,0,0,60,56,1,0,0,0,60,59,1,0,0,0,61,5,1,0,0,0,62,
        63,5,5,0,0,63,64,5,2,0,0,64,65,3,18,9,0,65,66,5,3,0,0,66,69,3,16,
        8,0,67,68,5,6,0,0,68,70,3,16,8,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        7,1,0,0,0,71,72,5,7,0,0,72,73,5,2,0,0,73,74,3,18,9,0,74,75,5,3,0,
        0,75,76,3,16,8,0,76,9,1,0,0,0,77,78,5,1,0,0,78,81,5,25,0,0,79,80,
        5,8,0,0,80,82,3,18,9,0,81,79,1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,
        83,84,5,25,0,0,84,85,5,8,0,0,85,86,3,18,9,0,86,13,1,0,0,0,87,88,
        5,9,0,0,88,89,3,18,9,0,89,15,1,0,0,0,90,94,5,10,0,0,91,93,3,4,2,
        0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,
        1,0,0,0,96,94,1,0,0,0,97,98,5,11,0,0,98,17,1,0,0,0,99,100,3,20,10,
        0,100,19,1,0,0,0,101,106,3,22,11,0,102,103,5,12,0,0,103,105,3,22,
        11,0,104,102,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,
        0,0,107,21,1,0,0,0,108,106,1,0,0,0,109,114,3,24,12,0,110,111,5,13,
        0,0,111,113,3,24,12,0,112,110,1,0,0,0,113,116,1,0,0,0,114,112,1,
        0,0,0,114,115,1,0,0,0,115,23,1,0,0,0,116,114,1,0,0,0,117,122,3,26,
        13,0,118,119,7,0,0,0,119,121,3,26,13,0,120,118,1,0,0,0,121,124,1,
        0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,25,1,0,0,0,124,122,1,0,
        0,0,125,130,3,28,14,0,126,127,7,1,0,0,127,129,3,28,14,0,128,126,
        1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,27,1,
        0,0,0,132,130,1,0,0,0,133,138,3,30,15,0,134,135,7,2,0,0,135,137,
        3,30,15,0,136,134,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,
        1,0,0,0,139,29,1,0,0,0,140,138,1,0,0,0,141,146,3,32,16,0,142,143,
        7,3,0,0,143,145,3,32,16,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,31,1,0,0,0,148,146,1,0,0,0,149,150,7,
        4,0,0,150,153,3,32,16,0,151,153,3,34,17,0,152,149,1,0,0,0,152,151,
        1,0,0,0,153,33,1,0,0,0,154,155,5,2,0,0,155,156,3,18,9,0,156,157,
        5,3,0,0,157,161,1,0,0,0,158,161,5,25,0,0,159,161,5,26,0,0,160,154,
        1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,35,1,0,0,0,14,38,40,
        60,69,81,94,106,114,122,130,138,146,152,160
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'('", "')'", "';'", "'if'", 
                     "'else'", "'while'", "'='", "'return'", "'{'", "'}'", 
                     "'||'", "'&&'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'+'", "'-'", "'*'", "'/'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_function = 1
    RULE_statement = 2
    RULE_ifStatement = 3
    RULE_whileStatement = 4
    RULE_declaration = 5
    RULE_assignment = 6
    RULE_returnStatement = 7
    RULE_block = 8
    RULE_expression = 9
    RULE_logicalOr = 10
    RULE_logicalAnd = 11
    RULE_equality = 12
    RULE_relational = 13
    RULE_additive = 14
    RULE_multiplicative = 15
    RULE_unary = 16
    RULE_primary = 17

    ruleNames =  [ "prog", "function", "statement", "ifStatement", "whileStatement", 
                   "declaration", "assignment", "returnStatement", "block", 
                   "expression", "logicalOr", "logicalAnd", "equality", 
                   "relational", "additive", "multiplicative", "unary", 
                   "primary" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    ID=25
    INT=26
    WS=27
    COMMENT=28
    LINE_COMMENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.FunctionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.FunctionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SimpleLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.function()
                    pass

                elif la_ == 2:
                    self.state = 37
                    self.statement()
                    pass


                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33555122) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = SimpleLangParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(SimpleLangParser.T__0)
            self.state = 43
            self.match(SimpleLangParser.ID)
            self.state = 44
            self.match(SimpleLangParser.T__1)
            self.state = 45
            self.match(SimpleLangParser.T__2)
            self.state = 46
            self.block()
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

        def ifStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.WhileStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SimpleLangParser.AssignmentContext,0)


        def declaration(self):
            return self.getTypedRuleContext(SimpleLangParser.DeclarationContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(SimpleLangParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.whileStatement()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.assignment()
                self.state = 51
                self.match(SimpleLangParser.T__3)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.declaration()
                self.state = 54
                self.match(SimpleLangParser.T__3)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.returnStatement()
                self.state = 57
                self.match(SimpleLangParser.T__3)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.match(SimpleLangParser.T__3)
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.BlockContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SimpleLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SimpleLangParser.T__4)
            self.state = 63
            self.match(SimpleLangParser.T__1)
            self.state = 64
            self.expression()
            self.state = 65
            self.match(SimpleLangParser.T__2)
            self.state = 66
            self.block()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 67
                self.match(SimpleLangParser.T__5)
                self.state = 68
                self.block()


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

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = SimpleLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(SimpleLangParser.T__6)
            self.state = 72
            self.match(SimpleLangParser.T__1)
            self.state = 73
            self.expression()
            self.state = 74
            self.match(SimpleLangParser.T__2)
            self.state = 75
            self.block()
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

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = SimpleLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SimpleLangParser.T__0)
            self.state = 78
            self.match(SimpleLangParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 79
                self.match(SimpleLangParser.T__7)
                self.state = 80
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SimpleLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SimpleLangParser.ID)
            self.state = 84
            self.match(SimpleLangParser.T__7)
            self.state = 85
            self.expression()
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

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = SimpleLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SimpleLangParser.T__8)
            self.state = 88
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SimpleLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SimpleLangParser.T__9)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33555122) != 0):
                self.state = 91
                self.statement()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(SimpleLangParser.T__10)
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

        def logicalOr(self):
            return self.getTypedRuleContext(SimpleLangParser.LogicalOrContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SimpleLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.logicalOr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.LogicalAndContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_logicalOr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOr(self):

        localctx = SimpleLangParser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.logicalAnd()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 102
                self.match(SimpleLangParser.T__11)
                self.state = 103
                self.logicalAnd()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.EqualityContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.EqualityContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_logicalAnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicalAnd(self):

        localctx = SimpleLangParser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.equality()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 110
                self.match(SimpleLangParser.T__12)
                self.state = 111
                self.equality()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.RelationalContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.RelationalContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_equality

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = SimpleLangParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.relational()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.relational()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.AdditiveContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = SimpleLangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.additive()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                self.state = 126
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 127
                self.additive()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.MultiplicativeContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_additive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = SimpleLangParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.multiplicative()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 134
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 135
                self.multiplicative()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.UnaryContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.UnaryContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_multiplicative

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = SimpleLangParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.unary()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.unary()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(SimpleLangParser.UnaryContext,0)


        def primary(self):
            return self.getTypedRuleContext(SimpleLangParser.PrimaryContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_unary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = SimpleLangParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==21 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.unary()
                pass
            elif token in [2, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.primary()
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


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def INT(self):
            return self.getToken(SimpleLangParser.INT, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = SimpleLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(SimpleLangParser.T__1)
                self.state = 155
                self.expression()
                self.state = 156
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(SimpleLangParser.ID)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(SimpleLangParser.INT)
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





