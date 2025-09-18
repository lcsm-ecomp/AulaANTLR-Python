# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#programa.
    def enterPrograma(self, ctx:ExprParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ExprParser#programa.
    def exitPrograma(self, ctx:ExprParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ExprParser#dec.
    def enterDec(self, ctx:ExprParser.DecContext):
        pass

    # Exit a parse tree produced by ExprParser#dec.
    def exitDec(self, ctx:ExprParser.DecContext):
        pass


    # Enter a parse tree produced by ExprParser#Print.
    def enterPrint(self, ctx:ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#Print.
    def exitPrint(self, ctx:ExprParser.PrintContext):
        pass


    # Enter a parse tree produced by ExprParser#Atrib.
    def enterAtrib(self, ctx:ExprParser.AtribContext):
        pass

    # Exit a parse tree produced by ExprParser#Atrib.
    def exitAtrib(self, ctx:ExprParser.AtribContext):
        pass


    # Enter a parse tree produced by ExprParser#For.
    def enterFor(self, ctx:ExprParser.ForContext):
        pass

    # Exit a parse tree produced by ExprParser#For.
    def exitFor(self, ctx:ExprParser.ForContext):
        pass


    # Enter a parse tree produced by ExprParser#Group.
    def enterGroup(self, ctx:ExprParser.GroupContext):
        pass

    # Exit a parse tree produced by ExprParser#Group.
    def exitGroup(self, ctx:ExprParser.GroupContext):
        pass


    # Enter a parse tree produced by ExprParser#Mult.
    def enterMult(self, ctx:ExprParser.MultContext):
        pass

    # Exit a parse tree produced by ExprParser#Mult.
    def exitMult(self, ctx:ExprParser.MultContext):
        pass


    # Enter a parse tree produced by ExprParser#Var.
    def enterVar(self, ctx:ExprParser.VarContext):
        pass

    # Exit a parse tree produced by ExprParser#Var.
    def exitVar(self, ctx:ExprParser.VarContext):
        pass


    # Enter a parse tree produced by ExprParser#Const.
    def enterConst(self, ctx:ExprParser.ConstContext):
        pass

    # Exit a parse tree produced by ExprParser#Const.
    def exitConst(self, ctx:ExprParser.ConstContext):
        pass


    # Enter a parse tree produced by ExprParser#Soma.
    def enterSoma(self, ctx:ExprParser.SomaContext):
        pass

    # Exit a parse tree produced by ExprParser#Soma.
    def exitSoma(self, ctx:ExprParser.SomaContext):
        pass



del ExprParser