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
        4,1,8,31,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,26,8,1,10,1,12,
        1,29,9,1,1,1,0,1,2,2,0,2,0,0,33,0,4,1,0,0,0,2,14,1,0,0,0,4,5,3,2,
        1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,0,8,15,5,6,0,0,9,15,5,2,0,
        0,10,11,5,3,0,0,11,12,3,2,1,0,12,13,5,4,0,0,13,15,1,0,0,0,14,7,1,
        0,0,0,14,9,1,0,0,0,14,10,1,0,0,0,15,27,1,0,0,0,16,17,10,6,0,0,17,
        18,5,1,0,0,18,26,3,2,1,7,19,20,10,5,0,0,20,21,5,7,0,0,21,26,3,2,
        1,6,22,23,10,4,0,0,23,24,5,8,0,0,24,26,3,2,1,5,25,16,1,0,0,0,25,
        19,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,
        0,28,3,1,0,0,0,29,27,1,0,0,0,3,14,25,27
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'x'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BRANCOS", "NUM", "OPM", "OPS" ]

    RULE_start = 0
    RULE_exp = 1

    ruleNames =  [ "start", "exp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    BRANCOS=5
    NUM=6
    OPM=7
    OPS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ExprParser.ExpContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = ExprParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.exp(0)
            self.state = 5
            self.match(ExprParser.EOF)
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


    class SomContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.op = None # Token
            self.d = None # ExpContext
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpContext,i)

        def OPS(self):
            return self.getToken(ExprParser.OPS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSom" ):
                listener.enterSom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSom" ):
                listener.exitSom(self)


    class GroupContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(ExprParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)


    class PotContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.op = None # Token
            self.d = None # ExpContext
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPot" ):
                listener.enterPot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPot" ):
                listener.exitPot(self)


    class MulContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.e = None # ExpContext
            self.op = None # Token
            self.d = None # ExpContext
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpContext,i)

        def OPM(self):
            return self.getToken(ExprParser.OPM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)


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


    class VarXContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarX" ):
                listener.enterVarX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarX" ):
                listener.exitVarX(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = ExprParser.ConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                localctx.valor = self.match(ExprParser.NUM)
                pass
            elif token in [2]:
                localctx = ExprParser.VarXContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(ExprParser.T__1)
                pass
            elif token in [3]:
                localctx = ExprParser.GroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(ExprParser.T__2)
                self.state = 11
                localctx.e = self.exp(0)
                self.state = 12
                self.match(ExprParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 25
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.PotContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 16
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 17
                        localctx.op = self.match(ExprParser.T__0)
                        self.state = 18
                        localctx.d = self.exp(7)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MulContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 19
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 20
                        localctx.op = self.match(ExprParser.OPM)
                        self.state = 21
                        localctx.d = self.exp(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.SomContext(self, ExprParser.ExpContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 22
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 23
                        localctx.op = self.match(ExprParser.OPS)
                        self.state = 24
                        localctx.d = self.exp(5)
                        pass

             
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self._predicates[1] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




