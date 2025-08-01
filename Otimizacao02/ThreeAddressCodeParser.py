# Generated from ThreeAddressCode.g4 by ANTLR 4.13.2
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
        4,1,14,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,3,0,16,8,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,1,1,1,1,1,1,1,
        1,1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,51,8,6,1,6,1,6,1,6,1,6,1,6,1,6,
        5,6,59,8,6,10,6,12,6,62,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,2,1,0,
        7,8,1,0,9,10,66,0,20,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,34,1,0,
        0,0,8,37,1,0,0,0,10,40,1,0,0,0,12,50,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,19,5,13,0,0,18,15,1,0,0,0,
        19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,1,1,0,0,0,22,20,1,0,
        0,0,23,29,3,4,2,0,24,29,3,6,3,0,25,29,3,8,4,0,26,29,3,10,5,0,27,
        29,5,13,0,0,28,23,1,0,0,0,28,24,1,0,0,0,28,25,1,0,0,0,28,26,1,0,
        0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,11,0,0,31,32,5,1,0,0,32,33,
        3,12,6,0,33,5,1,0,0,0,34,35,5,2,0,0,35,36,3,12,6,0,36,7,1,0,0,0,
        37,38,5,11,0,0,38,39,5,3,0,0,39,9,1,0,0,0,40,41,5,4,0,0,41,42,5,
        11,0,0,42,11,1,0,0,0,43,44,6,6,-1,0,44,45,5,5,0,0,45,46,3,12,6,0,
        46,47,5,6,0,0,47,51,1,0,0,0,48,51,5,11,0,0,49,51,5,12,0,0,50,43,
        1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,60,1,0,0,0,52,53,10,4,0,0,
        53,54,7,0,0,0,54,59,3,12,6,5,55,56,10,3,0,0,56,57,7,1,0,0,57,59,
        3,12,6,4,58,52,1,0,0,0,58,55,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,
        60,61,1,0,0,0,61,13,1,0,0,0,62,60,1,0,0,0,6,15,20,28,50,58,60
    ]

class ThreeAddressCodeParser ( Parser ):

    grammarFileName = "ThreeAddressCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'return'", "':'", "'goto'", "'('", 
                     "')'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "EOL", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_assignment = 2
    RULE_return_stmt = 3
    RULE_label = 4
    RULE_goto = 5
    RULE_expr = 6

    ruleNames =  [ "program", "line", "assignment", "return_stmt", "label", 
                   "goto", "expr" ]

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
    ID=11
    INT=12
    EOL=13
    WS=14

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

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(ThreeAddressCodeParser.EOL)
            else:
                return self.getToken(ThreeAddressCodeParser.EOL, i)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.LineContext,i)


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ThreeAddressCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10260) != 0):
                self.state = 15
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 14
                    self.line()


                self.state = 17
                self.match(ThreeAddressCodeParser.EOL)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.AssignmentContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.Return_stmtContext,0)


        def label(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.LabelContext,0)


        def goto(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.GotoContext,0)


        def EOL(self):
            return self.getToken(ThreeAddressCodeParser.EOL, 0)

        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = ThreeAddressCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.return_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.label()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.goto()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.match(ThreeAddressCodeParser.EOL)
                pass


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
            return self.getToken(ThreeAddressCodeParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ThreeAddressCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ThreeAddressCodeParser.ID)
            self.state = 31
            self.match(ThreeAddressCodeParser.T__0)
            self.state = 32
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ThreeAddressCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ThreeAddressCodeParser.T__1)
            self.state = 35
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ThreeAddressCodeParser.ID, 0)

        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = ThreeAddressCodeParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ThreeAddressCodeParser.ID)
            self.state = 38
            self.match(ThreeAddressCodeParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ThreeAddressCodeParser.ID, 0)

        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_goto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto" ):
                return visitor.visitGoto(self)
            else:
                return visitor.visitChildren(self)




    def goto(self):

        localctx = ThreeAddressCodeParser.GotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ThreeAddressCodeParser.T__3)
            self.state = 41
            self.match(ThreeAddressCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ThreeAddressCodeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BinaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ThreeAddressCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ThreeAddressCodeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpr" ):
                return visitor.visitBinaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ThreeAddressCodeParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ThreeAddressCodeParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ThreeAddressCodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ThreeAddressCodeParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ThreeAddressCodeParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = ThreeAddressCodeParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(ThreeAddressCodeParser.T__4)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(ThreeAddressCodeParser.T__5)
                pass
            elif token in [11]:
                localctx = ThreeAddressCodeParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(ThreeAddressCodeParser.ID)
                pass
            elif token in [12]:
                localctx = ThreeAddressCodeParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(ThreeAddressCodeParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ThreeAddressCodeParser.BinaryExprContext(self, ThreeAddressCodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ThreeAddressCodeParser.BinaryExprContext(self, ThreeAddressCodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(4)
                        pass

             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




