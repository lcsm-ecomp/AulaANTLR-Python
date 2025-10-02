# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#start.
    def enterStart(self, ctx:ExprParser.StartContext):
        pass

    # Exit a parse tree produced by ExprParser#start.
    def exitStart(self, ctx:ExprParser.StartContext):
        pass


    # Enter a parse tree produced by ExprParser#Som.
    def enterSom(self, ctx:ExprParser.SomContext):
        pass

    # Exit a parse tree produced by ExprParser#Som.
    def exitSom(self, ctx:ExprParser.SomContext):
        pass


    # Enter a parse tree produced by ExprParser#Group.
    def enterGroup(self, ctx:ExprParser.GroupContext):
        pass

    # Exit a parse tree produced by ExprParser#Group.
    def exitGroup(self, ctx:ExprParser.GroupContext):
        pass


    # Enter a parse tree produced by ExprParser#Pot.
    def enterPot(self, ctx:ExprParser.PotContext):
        pass

    # Exit a parse tree produced by ExprParser#Pot.
    def exitPot(self, ctx:ExprParser.PotContext):
        pass


    # Enter a parse tree produced by ExprParser#Mul.
    def enterMul(self, ctx:ExprParser.MulContext):
        pass

    # Exit a parse tree produced by ExprParser#Mul.
    def exitMul(self, ctx:ExprParser.MulContext):
        pass


    # Enter a parse tree produced by ExprParser#Const.
    def enterConst(self, ctx:ExprParser.ConstContext):
        pass

    # Exit a parse tree produced by ExprParser#Const.
    def exitConst(self, ctx:ExprParser.ConstContext):
        pass


    # Enter a parse tree produced by ExprParser#VarX.
    def enterVarX(self, ctx:ExprParser.VarXContext):
        pass

    # Exit a parse tree produced by ExprParser#VarX.
    def exitVarX(self, ctx:ExprParser.VarXContext):
        pass



del ExprParser