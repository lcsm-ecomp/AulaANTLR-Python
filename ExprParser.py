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
        4,1,15,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,4,0,15,8,0,11,0,12,0,16,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,
        42,8,2,11,2,12,2,43,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,57,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,65,8,3,10,3,12,3,68,9,3,
        1,3,0,1,6,4,0,2,4,6,0,0,74,0,9,1,0,0,0,2,20,1,0,0,0,4,47,1,0,0,0,
        6,56,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,
        11,12,1,0,0,0,12,14,1,0,0,0,13,15,3,4,2,0,14,13,1,0,0,0,15,16,1,
        0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,18,1,0,0,0,18,19,5,0,0,1,19,
        1,1,0,0,0,20,21,5,7,0,0,21,22,5,10,0,0,22,23,5,1,0,0,23,3,1,0,0,
        0,24,25,5,8,0,0,25,26,3,6,3,0,26,27,5,1,0,0,27,48,1,0,0,0,28,29,
        5,10,0,0,29,30,5,2,0,0,30,31,3,6,3,0,31,32,5,1,0,0,32,48,1,0,0,0,
        33,34,5,6,0,0,34,35,5,10,0,0,35,36,5,2,0,0,36,37,5,9,0,0,37,38,5,
        3,0,0,38,39,5,9,0,0,39,41,5,4,0,0,40,42,3,4,2,0,41,40,1,0,0,0,42,
        43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,5,0,
        0,46,48,1,0,0,0,47,24,1,0,0,0,47,28,1,0,0,0,47,33,1,0,0,0,48,5,1,
        0,0,0,49,50,6,3,-1,0,50,57,5,9,0,0,51,57,5,10,0,0,52,53,5,13,0,0,
        53,54,3,6,3,0,54,55,5,14,0,0,55,57,1,0,0,0,56,49,1,0,0,0,56,51,1,
        0,0,0,56,52,1,0,0,0,57,66,1,0,0,0,58,59,10,3,0,0,59,60,5,12,0,0,
        60,65,3,6,3,4,61,62,10,2,0,0,62,63,5,11,0,0,63,65,3,6,3,3,64,58,
        1,0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,
        67,7,1,0,0,0,68,66,1,0,0,0,7,11,16,43,47,56,64,66
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'to'", "'do'", "'end'", 
                     "'for'", "'var'", "'print'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FOR", "VAR", "PRINT", "NUM", 
                      "ID", "OP1", "OP2", "AP", "FP", "SPACE" ]

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
    FOR=6
    VAR=7
    PRINT=8
    NUM=9
    ID=10
    OP1=11
    OP2=12
    AP=13
    FP=14
    SPACE=15

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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                localctx._dec = self.dec()
                localctx.declaracoes.append(localctx._dec)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                localctx._com = self.com()
                localctx.comandos.append(localctx._com)
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1344) != 0)):
                    break

            self.state = 18
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
            self.nome = None # Token

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

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
            self.state = 20
            self.match(ExprParser.VAR)
            self.state = 21
            localctx.nome = self.match(ExprParser.ID)
            self.state = 22
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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = ExprParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(ExprParser.PRINT)
                self.state = 25
                localctx.e = self.exp(0)
                self.state = 26
                self.match(ExprParser.T__0)
                pass
            elif token in [10]:
                localctx = ExprParser.AtribContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                localctx.nome = self.match(ExprParser.ID)
                self.state = 29
                self.match(ExprParser.T__1)
                self.state = 30
                localctx.valor = self.exp(0)
                self.state = 31
                self.match(ExprParser.T__0)
                pass
            elif token in [6]:
                localctx = ExprParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.match(ExprParser.FOR)
                self.state = 34
                localctx.nome = self.match(ExprParser.ID)
                self.state = 35
                self.match(ExprParser.T__1)
                self.state = 36
                self.match(ExprParser.NUM)
                self.state = 37
                self.match(ExprParser.T__2)
                self.state = 38
                self.match(ExprParser.NUM)
                self.state = 39
                self.match(ExprParser.T__3)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 40
                    localctx._com = self.com()
                    localctx.c.append(localctx._com)
                    self.state = 43 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1344) != 0)):
                        break

                self.state = 45
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


    class ConstContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.valor = None # Token
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)


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



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = ExprParser.ConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 50
                localctx.valor = self.match(ExprParser.NUM)
                pass
            elif token in [10]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                localctx.nome = self.match(ExprParser.ID)
                pass
            elif token in [13]:
                localctx = ExprParser.GroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(ExprParser.AP)
                self.state = 53
                localctx.e = self.exp(0)
                self.state = 54
                self.match(ExprParser.FP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.MultContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 58
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 59
                        localctx.o = self.match(ExprParser.OP2)
                        self.state = 60
                        localctx.d = self.exp(4)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.SomaContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 61
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 62
                        localctx.o = self.match(ExprParser.OP1)
                        self.state = 63
                        localctx.d = self.exp(3)
                        pass

             
                self.state = 68
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




