# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,46,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,
        5,4,5,31,8,5,11,5,12,5,32,1,5,1,5,4,5,37,8,5,11,5,12,5,38,3,5,41,
        8,5,1,6,1,6,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,
        4,2,0,9,10,32,32,1,0,48,57,2,0,42,42,47,47,2,0,43,43,45,45,48,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,
        0,0,0,7,23,1,0,0,0,9,25,1,0,0,0,11,30,1,0,0,0,13,42,1,0,0,0,15,44,
        1,0,0,0,17,18,5,94,0,0,18,2,1,0,0,0,19,20,5,120,0,0,20,4,1,0,0,0,
        21,22,5,40,0,0,22,6,1,0,0,0,23,24,5,41,0,0,24,8,1,0,0,0,25,26,7,
        0,0,0,26,27,1,0,0,0,27,28,6,4,0,0,28,10,1,0,0,0,29,31,7,1,0,0,30,
        29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,40,1,0,0,
        0,34,36,5,46,0,0,35,37,7,1,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,34,1,0,0,0,40,41,1,0,0,0,
        41,12,1,0,0,0,42,43,7,2,0,0,43,14,1,0,0,0,44,45,7,3,0,0,45,16,1,
        0,0,0,4,0,32,38,40,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    BRANCOS = 5
    NUM = 6
    OPM = 7
    OPS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'^'", "'x'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "BRANCOS", "NUM", "OPM", "OPS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "BRANCOS", "NUM", "OPM", 
                  "OPS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


