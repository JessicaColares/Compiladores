# Generated from SimpleLang.g by ANTLR 4.13.2
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
        4,1,38,193,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,50,8,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,5,3,59,8,3,10,3,12,3,62,9,3,3,3,64,8,3,1,4,1,4,1,4,1,5,1,5,
        1,5,5,5,72,8,5,10,5,12,5,75,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,3,7,86,8,7,1,7,1,7,1,7,1,7,3,7,92,8,7,5,7,94,8,7,10,7,12,7,97,
        9,7,1,8,1,8,1,8,1,8,1,8,3,8,104,8,8,1,9,1,9,1,9,1,10,1,10,3,10,111,
        8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,122,8,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,154,8,13,1,13,1,13,1,13,1,13,1,13,3,13,
        161,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,172,8,
        13,10,13,12,13,175,9,13,1,14,1,14,3,14,179,8,14,1,14,1,14,1,14,3,
        14,184,8,14,5,14,186,8,14,10,14,12,14,189,9,14,1,15,1,15,1,15,0,
        1,26,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,6,1,0,24,27,
        1,0,33,35,1,0,13,15,1,0,16,17,1,0,18,23,2,0,4,4,31,32,209,0,36,1,
        0,0,0,2,41,1,0,0,0,4,45,1,0,0,0,6,63,1,0,0,0,8,65,1,0,0,0,10,68,
        1,0,0,0,12,78,1,0,0,0,14,82,1,0,0,0,16,103,1,0,0,0,18,105,1,0,0,
        0,20,108,1,0,0,0,22,114,1,0,0,0,24,123,1,0,0,0,26,160,1,0,0,0,28,
        178,1,0,0,0,30,190,1,0,0,0,32,35,3,2,1,0,33,35,3,4,2,0,34,32,1,0,
        0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,
        1,0,0,0,38,36,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,3,30,15,0,
        42,43,3,14,7,0,43,44,5,1,0,0,44,3,1,0,0,0,45,46,3,30,15,0,46,47,
        5,33,0,0,47,49,5,2,0,0,48,50,3,6,3,0,49,48,1,0,0,0,49,50,1,0,0,0,
        50,51,1,0,0,0,51,52,5,3,0,0,52,53,3,10,5,0,53,5,1,0,0,0,54,64,5,
        4,0,0,55,60,3,8,4,0,56,57,5,5,0,0,57,59,3,8,4,0,58,56,1,0,0,0,59,
        62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,
        0,63,54,1,0,0,0,63,55,1,0,0,0,64,7,1,0,0,0,65,66,3,30,15,0,66,67,
        5,33,0,0,67,9,1,0,0,0,68,73,5,6,0,0,69,72,3,12,6,0,70,72,3,16,8,
        0,71,69,1,0,0,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,7,0,0,77,11,1,0,0,0,
        78,79,3,30,15,0,79,80,3,14,7,0,80,81,5,1,0,0,81,13,1,0,0,0,82,85,
        5,33,0,0,83,84,5,8,0,0,84,86,3,26,13,0,85,83,1,0,0,0,85,86,1,0,0,
        0,86,95,1,0,0,0,87,88,5,5,0,0,88,91,5,33,0,0,89,90,5,8,0,0,90,92,
        3,26,13,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,87,1,0,0,
        0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,15,1,0,0,0,97,95,
        1,0,0,0,98,104,3,18,9,0,99,104,3,20,10,0,100,104,3,22,11,0,101,104,
        3,24,12,0,102,104,5,1,0,0,103,98,1,0,0,0,103,99,1,0,0,0,103,100,
        1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,17,1,0,0,0,105,106,3,
        26,13,0,106,107,5,1,0,0,107,19,1,0,0,0,108,110,5,9,0,0,109,111,3,
        26,13,0,110,109,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,
        5,1,0,0,113,21,1,0,0,0,114,115,5,10,0,0,115,116,5,2,0,0,116,117,
        3,26,13,0,117,118,5,3,0,0,118,121,3,10,5,0,119,120,5,11,0,0,120,
        122,3,10,5,0,121,119,1,0,0,0,121,122,1,0,0,0,122,23,1,0,0,0,123,
        124,5,12,0,0,124,125,5,2,0,0,125,126,3,26,13,0,126,127,5,3,0,0,127,
        128,3,10,5,0,128,25,1,0,0,0,129,130,6,13,-1,0,130,131,5,33,0,0,131,
        132,5,8,0,0,132,161,3,26,13,11,133,134,5,33,0,0,134,135,7,0,0,0,
        135,161,3,26,13,10,136,137,5,28,0,0,137,161,5,33,0,0,138,139,5,29,
        0,0,139,161,5,33,0,0,140,141,5,30,0,0,141,142,5,2,0,0,142,143,5,
        36,0,0,143,144,5,5,0,0,144,145,7,1,0,0,145,161,5,3,0,0,146,161,5,
        33,0,0,147,161,5,34,0,0,148,161,5,35,0,0,149,161,5,36,0,0,150,151,
        5,33,0,0,151,153,5,2,0,0,152,154,3,28,14,0,153,152,1,0,0,0,153,154,
        1,0,0,0,154,155,1,0,0,0,155,161,5,3,0,0,156,157,5,2,0,0,157,158,
        3,26,13,0,158,159,5,3,0,0,159,161,1,0,0,0,160,129,1,0,0,0,160,133,
        1,0,0,0,160,136,1,0,0,0,160,138,1,0,0,0,160,140,1,0,0,0,160,146,
        1,0,0,0,160,147,1,0,0,0,160,148,1,0,0,0,160,149,1,0,0,0,160,150,
        1,0,0,0,160,156,1,0,0,0,161,173,1,0,0,0,162,163,10,14,0,0,163,164,
        7,2,0,0,164,172,3,26,13,15,165,166,10,13,0,0,166,167,7,3,0,0,167,
        172,3,26,13,14,168,169,10,12,0,0,169,170,7,4,0,0,170,172,3,26,13,
        13,171,162,1,0,0,0,171,165,1,0,0,0,171,168,1,0,0,0,172,175,1,0,0,
        0,173,171,1,0,0,0,173,174,1,0,0,0,174,27,1,0,0,0,175,173,1,0,0,0,
        176,179,3,26,13,0,177,179,5,36,0,0,178,176,1,0,0,0,178,177,1,0,0,
        0,179,187,1,0,0,0,180,183,5,5,0,0,181,184,3,26,13,0,182,184,5,36,
        0,0,183,181,1,0,0,0,183,182,1,0,0,0,184,186,1,0,0,0,185,180,1,0,
        0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,29,1,0,0,
        0,189,187,1,0,0,0,190,191,7,5,0,0,191,31,1,0,0,0,20,34,36,49,60,
        63,71,73,85,91,95,103,110,121,153,160,171,173,178,183,187
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'void'", "','", 
                     "'{'", "'}'", "'='", "'return'", "'if'", "'else'", 
                     "'while'", "'*'", "'/'", "'%'", "'+'", "'-'", "'<'", 
                     "'<='", "'>'", "'>='", "'=='", "'!='", "'*='", "'/='", 
                     "'+='", "'-='", "'++'", "'--'", "'printf'", "'int'", 
                     "'char'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "CHAR", "STRING", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_global_declaration = 1
    RULE_function = 2
    RULE_params = 3
    RULE_param = 4
    RULE_block = 5
    RULE_declaration = 6
    RULE_var_list = 7
    RULE_statement = 8
    RULE_exprStmt = 9
    RULE_returnStmt = 10
    RULE_ifStmt = 11
    RULE_whileStmt = 12
    RULE_expression = 13
    RULE_argList = 14
    RULE_type = 15

    ruleNames =  [ "program", "global_declaration", "function", "params", 
                   "param", "block", "declaration", "var_list", "statement", 
                   "exprStmt", "returnStmt", "ifStmt", "whileStmt", "expression", 
                   "argList", "type" ]

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
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    ID=33
    INT=34
    CHAR=35
    STRING=36
    WS=37
    COMMENT=38

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
            return self.getToken(SimpleLangParser.EOF, 0)

        def global_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Global_declarationContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Global_declarationContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.FunctionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.FunctionContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SimpleLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6442450960) != 0):
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 32
                    self.global_declaration()
                    pass

                elif la_ == 2:
                    self.state = 33
                    self.function()
                    pass


                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(SimpleLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def var_list(self):
            return self.getTypedRuleContext(SimpleLangParser.Var_listContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_global_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_declaration" ):
                return visitor.visitGlobal_declaration(self)
            else:
                return visitor.visitChildren(self)




    def global_declaration(self):

        localctx = SimpleLangParser.Global_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_global_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.type_()
            self.state = 42
            self.var_list()
            self.state = 43
            self.match(SimpleLangParser.T__0)
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

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(SimpleLangParser.ParamsContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = SimpleLangParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.type_()
            self.state = 46
            self.match(SimpleLangParser.ID)
            self.state = 47
            self.match(SimpleLangParser.T__1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6442450960) != 0):
                self.state = 48
                self.params()


            self.state = 51
            self.match(SimpleLangParser.T__2)
            self.state = 52
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ParamContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = SimpleLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(SimpleLangParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.param()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 56
                    self.match(SimpleLangParser.T__4)
                    self.state = 57
                    self.param()
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = SimpleLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.type_()
            self.state = 66
            self.match(SimpleLangParser.ID)
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

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.DeclarationContext,i)


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
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SimpleLangParser.T__5)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137170523670) != 0):
                self.state = 71
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4, 31, 32]:
                    self.state = 69
                    self.declaration()
                    pass
                elif token in [1, 2, 9, 10, 12, 28, 29, 30, 33, 34, 35, 36]:
                    self.state = 70
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(SimpleLangParser.T__6)
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

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def var_list(self):
            return self.getTypedRuleContext(SimpleLangParser.Var_listContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = SimpleLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.type_()
            self.state = 79
            self.var_list()
            self.state = 80
            self.match(SimpleLangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.ID)
            else:
                return self.getToken(SimpleLangParser.ID, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = SimpleLangParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(SimpleLangParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 83
                self.match(SimpleLangParser.T__7)
                self.state = 84
                self.expression(0)


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 87
                self.match(SimpleLangParser.T__4)
                self.state = 88
                self.match(SimpleLangParser.ID)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 89
                    self.match(SimpleLangParser.T__7)
                    self.state = 90
                    self.expression(0)


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def exprStmt(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(SimpleLangParser.ReturnStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(SimpleLangParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(SimpleLangParser.WhileStmtContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 28, 29, 30, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.exprStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.returnStmt()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.ifStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.whileStmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.match(SimpleLangParser.T__0)
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


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_exprStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = SimpleLangParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.expression(0)
            self.state = 106
            self.match(SimpleLangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = SimpleLangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(SimpleLangParser.T__8)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130728067076) != 0):
                self.state = 109
                self.expression(0)


            self.state = 112
            self.match(SimpleLangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
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
            return SimpleLangParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = SimpleLangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(SimpleLangParser.T__9)
            self.state = 115
            self.match(SimpleLangParser.T__1)
            self.state = 116
            self.expression(0)
            self.state = 117
            self.match(SimpleLangParser.T__2)
            self.state = 118
            self.block()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 119
                self.match(SimpleLangParser.T__10)
                self.state = 120
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = SimpleLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(SimpleLangParser.T__11)
            self.state = 124
            self.match(SimpleLangParser.T__1)
            self.state = 125
            self.expression(0)
            self.state = 126
            self.match(SimpleLangParser.T__2)
            self.state = 127
            self.block()
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


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CompoundAssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundAssignExpr" ):
                return visitor.visitCompoundAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class CharExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(SimpleLangParser.CHAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharExpr" ):
                return visitor.visitCharExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SimpleLangParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class PreIncExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreIncExpr" ):
                return visitor.visitPreIncExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class PreDecExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreDecExpr" ):
                return visitor.visitPreDecExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrintfExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)
        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def INT(self):
            return self.getToken(SimpleLangParser.INT, 0)
        def CHAR(self):
            return self.getToken(SimpleLangParser.CHAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintfExpr" ):
                return visitor.visitPrintfExpr(self)
            else:
                return visitor.visitChildren(self)


    class CallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def argList(self):
            return self.getTypedRuleContext(SimpleLangParser.ArgListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallExpr" ):
                return visitor.visitCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 130
                self.match(SimpleLangParser.ID)
                self.state = 131
                self.match(SimpleLangParser.T__7)
                self.state = 132
                self.expression(11)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.CompoundAssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(SimpleLangParser.ID)
                self.state = 134
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 135
                self.expression(10)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.PreIncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.match(SimpleLangParser.T__27)
                self.state = 137
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.PreDecExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(SimpleLangParser.T__28)
                self.state = 139
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.PrintfExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(SimpleLangParser.T__29)
                self.state = 141
                self.match(SimpleLangParser.T__1)
                self.state = 142
                self.match(SimpleLangParser.STRING)
                self.state = 143
                self.match(SimpleLangParser.T__4)
                self.state = 144
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.match(SimpleLangParser.T__2)
                pass

            elif la_ == 6:
                localctx = SimpleLangParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 7:
                localctx = SimpleLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(SimpleLangParser.INT)
                pass

            elif la_ == 8:
                localctx = SimpleLangParser.CharExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(SimpleLangParser.CHAR)
                pass

            elif la_ == 9:
                localctx = SimpleLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(SimpleLangParser.STRING)
                pass

            elif la_ == 10:
                localctx = SimpleLangParser.CallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(SimpleLangParser.ID)
                self.state = 151
                self.match(SimpleLangParser.T__1)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130728067076) != 0):
                    self.state = 152
                    self.argList()


                self.state = 155
                self.match(SimpleLangParser.T__2)
                pass

            elif la_ == 11:
                localctx = SimpleLangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(SimpleLangParser.T__1)
                self.state = 157
                self.expression(0)
                self.state = 158
                self.match(SimpleLangParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 171
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivExprContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 162
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 163
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 164
                        self.expression(15)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubExprContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 165
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 166
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 167
                        self.expression(14)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.RelExprContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 169
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 170
                        self.expression(13)
                        pass

             
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.STRING)
            else:
                return self.getToken(SimpleLangParser.STRING, i)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = SimpleLangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 176
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 177
                self.match(SimpleLangParser.STRING)
                pass


            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 180
                self.match(SimpleLangParser.T__4)
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 181
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 182
                    self.match(SimpleLangParser.STRING)
                    pass


                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = SimpleLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6442450960) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         




