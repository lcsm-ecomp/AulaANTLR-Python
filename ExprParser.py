# Generated from Expr.g4 by ANTLR 4.13.2
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
        4,1,19,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        4,2,43,8,2,11,2,12,2,44,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,61,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,72,8,3,10,3,12,3,75,9,3,1,3,0,1,6,4,0,2,4,6,0,0,84,0,11,1,0,
        0,0,2,21,1,0,0,0,4,48,1,0,0,0,6,60,1,0,0,0,8,10,3,2,1,0,9,8,1,0,
        0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,15,1,0,0,0,13,11,
        1,0,0,0,14,16,3,4,2,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,
        17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,22,5,8,
        0,0,22,23,5,14,0,0,23,24,5,1,0,0,24,3,1,0,0,0,25,26,5,11,0,0,26,
        27,3,6,3,0,27,28,5,1,0,0,28,49,1,0,0,0,29,30,5,14,0,0,30,31,5,2,
        0,0,31,32,3,6,3,0,32,33,5,1,0,0,33,49,1,0,0,0,34,35,5,9,0,0,35,36,
        5,14,0,0,36,37,5,2,0,0,37,38,5,12,0,0,38,39,5,3,0,0,39,40,5,12,0,
        0,40,42,5,4,0,0,41,43,3,4,2,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,
        1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,5,5,0,0,47,49,1,0,0,0,
        48,25,1,0,0,0,48,29,1,0,0,0,48,34,1,0,0,0,49,5,1,0,0,0,50,51,6,3,
        -1,0,51,61,5,12,0,0,52,61,5,13,0,0,53,61,5,14,0,0,54,55,5,6,0,0,
        55,61,3,6,3,5,56,57,5,17,0,0,57,58,3,6,3,0,58,59,5,18,0,0,59,61,
        1,0,0,0,60,50,1,0,0,0,60,52,1,0,0,0,60,53,1,0,0,0,60,54,1,0,0,0,
        60,56,1,0,0,0,61,73,1,0,0,0,62,63,10,4,0,0,63,64,5,7,0,0,64,72,3,
        6,3,5,65,66,10,3,0,0,66,67,5,16,0,0,67,72,3,6,3,4,68,69,10,2,0,0,
        69,70,5,15,0,0,70,72,3,6,3,3,71,62,1,0,0,0,71,65,1,0,0,0,71,68,1,
        0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,7,1,0,0,0,75,
        73,1,0,0,0,7,11,17,44,48,60,71,73
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'to'", "'do'", "'end'", 
                     "'#'", "'++'", "<INVALID>", "'for'", "'var'", "'print'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TYPE", "FOR", "VAR", "PRINT", "NUM", "STR", "ID", 
                      "OP1", "OP2", "AP", "FP", "SPACE" ]

    RULE_programa = 0
    RULE_dec = 1
    RULE_com = 2
    RULE_exp = 3

    ruleNames =  [ "programa", "dec", "com", "exp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    TYPE=8
    FOR=9
    VAR=10
    PRINT=11
    NUM=12
    STR=13
    ID=14
    OP1=15
    OP2=16
    AP=17
    FP=18
    SPACE=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._dec = None # DecContext
            self.declaracoes = list() # of DecContexts
            self._com = None # ComContext
            self.comandos = list() # of ComContexts

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DecContext)
            else:
                return self.getTypedRuleContext(ExprParser.DecContext,i)


        def com(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ExprParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 8
                localctx._dec = self.dec()
                localctx.declaracoes.append(localctx._dec)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                localctx._com = self.com()
                localctx.comandos.append(localctx._com)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 18944) != 0)):
                    break

            self.state = 19
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tipo = None # Token
            self.nome = None # Token

        def TYPE(self):
            return self.getToken(ExprParser.TYPE, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_dec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec" ):
                listener.enterDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec" ):
                listener.exitDec(self)




    def dec(self):

        localctx = ExprParser.DecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            localctx.tipo = self.match(ExprParser.TYPE)
            self.state = 22
            localctx.nome = self.match(ExprParser.ID)
            self.state = 23
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_com

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(ComContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ComContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)
        def exp(self):
            return self.getTypedRuleContext(ExprParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)


    class AtribContext(ComContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ComContext
            super().__init__(parser)
            self.nome = None # Token
            self.valor = None # ExpContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def exp(self):
            return self.getTypedRuleContext(ExprParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtrib" ):
                listener.enterAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtrib" ):
                listener.exitAtrib(self)


    class ForContext(ComContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ComContext
            super().__init__(parser)
            self.nome = None # Token
            self._com = None # ComContext
            self.c = list() # of ComContexts
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)
        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NUM)
            else:
                return self.getToken(ExprParser.NUM, i)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def com(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)



    def com(self):

        localctx = ExprParser.ComContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_com)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = ExprParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(ExprParser.PRINT)
                self.state = 26
                localctx.e = self.exp(0)
                self.state = 27
                self.match(ExprParser.T__0)
                pass
            elif token in [14]:
                localctx = ExprParser.AtribContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                localctx.nome = self.match(ExprParser.ID)
                self.state = 30
                self.match(ExprParser.T__1)
                self.state = 31
                localctx.valor = self.exp(0)
                self.state = 32
                self.match(ExprParser.T__0)
                pass
            elif token in [9]:
                localctx = ExprParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(ExprParser.FOR)
                self.state = 35
                localctx.nome = self.match(ExprParser.ID)
                self.state = 36
                self.match(ExprParser.T__1)
                self.state = 37
                self.match(ExprParser.NUM)
                self.state = 38
                self.match(ExprParser.T__2)
                self.state = 39
                self.match(ExprParser.NUM)
                self.state = 40
                self.match(ExprParser.T__3)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 41
                    localctx._com = self.com()
                    localctx.c.append(localctx._com)
                    self.state = 44 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 18944) != 0)):
                        break

                self.state = 46
                self.match(ExprParser.T__4)
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ConstNumContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.valor = None # Token
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstNum" ):
                listener.enterConstNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstNum" ):
                listener.exitConstNum(self)


    class GroupContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.copyFrom(ctx)

        def AP(self):
            return self.getToken(ExprParser.AP, 0)
        def FP(self):
            return self.getToken(ExprParser.FP, 0)
        def exp(self):
            return self.getTypedRuleContext(ExprParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)


    class STRLengthContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(ExprParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTRLength" ):
                listener.enterSTRLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTRLength" ):
                listener.exitSTRLength(self)


    class STRConcatContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.d = None # ExpContext
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTRConcat" ):
                listener.enterSTRConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTRConcat" ):
                listener.exitSTRConcat(self)


    class MultContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.o = None # Token
            self.d = None # ExpContext
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpContext,i)

        def OP2(self):
            return self.getToken(ExprParser.OP2, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)


    class VarContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.nome = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)


    class SomaContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.o = None # Token
            self.d = None # ExpContext
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpContext,i)

        def OP1(self):
            return self.getToken(ExprParser.OP1, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoma" ):
                listener.enterSoma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoma" ):
                listener.exitSoma(self)


    class ConstStrContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.valor = None # Token
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(ExprParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstStr" ):
                listener.enterConstStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstStr" ):
                listener.exitConstStr(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = ExprParser.ConstNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 51
                localctx.valor = self.match(ExprParser.NUM)
                pass
            elif token in [13]:
                localctx = ExprParser.ConstStrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                localctx.valor = self.match(ExprParser.STR)
                pass
            elif token in [14]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                localctx.nome = self.match(ExprParser.ID)
                pass
            elif token in [6]:
                localctx = ExprParser.STRLengthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(ExprParser.T__5)
                self.state = 55
                localctx.e = self.exp(5)
                pass
            elif token in [17]:
                localctx = ExprParser.GroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(ExprParser.AP)
                self.state = 57
                localctx.e = self.exp(0)
                self.state = 58
                self.match(ExprParser.FP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.STRConcatContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 62
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 63
                        self.match(ExprParser.T__6)
                        self.state = 64
                        localctx.d = self.exp(5)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MultContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 65
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 66
                        localctx.o = self.match(ExprParser.OP2)
                        self.state = 67
                        localctx.d = self.exp(4)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.SomaContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 68
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 69
                        localctx.o = self.match(ExprParser.OP1)
                        self.state = 70
                        localctx.d = self.exp(3)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self._predicates[3] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




