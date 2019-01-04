# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procdecl.
    def visitProcdecl(self, ctx:MPParser.ProcdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdecl.
    def visitFuncdecl(self, ctx:MPParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardecl.
    def visitVardecl(self, ctx:MPParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paralist.
    def visitParalist(self, ctx:MPParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paradecl.
    def visitParadecl(self, ctx:MPParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stm.
    def visitStm(self, ctx:MPParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assstm.
    def visitAssstm(self, ctx:MPParser.AssstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstm.
    def visitIfstm(self, ctx:MPParser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstm.
    def visitForstm(self, ctx:MPParser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whlstm.
    def visitWhlstm(self, ctx:MPParser.WhlstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#brkstm.
    def visitBrkstm(self, ctx:MPParser.BrkstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#constm.
    def visitConstm(self, ctx:MPParser.ConstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#retstm.
    def visitRetstm(self, ctx:MPParser.RetstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#calstm.
    def visitCalstm(self, ctx:MPParser.CalstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#cpstm.
    def visitCpstm(self, ctx:MPParser.CpstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#witstm.
    def visitWitstm(self, ctx:MPParser.WitstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression1.
    def visitExpression1(self, ctx:MPParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression2.
    def visitExpression2(self, ctx:MPParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression3.
    def visitExpression3(self, ctx:MPParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression4.
    def visitExpression4(self, ctx:MPParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression5.
    def visitExpression5(self, ctx:MPParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vartype.
    def visitVartype(self, ctx:MPParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrvartype.
    def visitArrvartype(self, ctx:MPParser.ArrvartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idlist.
    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#blstm.
    def visitBlstm(self, ctx:MPParser.BlstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)



del MPParser