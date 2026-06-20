# Generated from SimpleLang.g by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#global_declaration.
    def visitGlobal_declaration(self, ctx:SimpleLangParser.Global_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#function.
    def visitFunction(self, ctx:SimpleLangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#params.
    def visitParams(self, ctx:SimpleLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#param.
    def visitParam(self, ctx:SimpleLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#block.
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#declaration.
    def visitDeclaration(self, ctx:SimpleLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#var_list.
    def visitVar_list(self, ctx:SimpleLangParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#exprStmt.
    def visitExprStmt(self, ctx:SimpleLangParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#returnStmt.
    def visitReturnStmt(self, ctx:SimpleLangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStmt.
    def visitIfStmt(self, ctx:SimpleLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#whileStmt.
    def visitWhileStmt(self, ctx:SimpleLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#compoundAssignExpr.
    def visitCompoundAssignExpr(self, ctx:SimpleLangParser.CompoundAssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#charExpr.
    def visitCharExpr(self, ctx:SimpleLangParser.CharExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#intExpr.
    def visitIntExpr(self, ctx:SimpleLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#addSubExpr.
    def visitAddSubExpr(self, ctx:SimpleLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parensExpr.
    def visitParensExpr(self, ctx:SimpleLangParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#stringExpr.
    def visitStringExpr(self, ctx:SimpleLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#preIncExpr.
    def visitPreIncExpr(self, ctx:SimpleLangParser.PreIncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#varExpr.
    def visitVarExpr(self, ctx:SimpleLangParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#preDecExpr.
    def visitPreDecExpr(self, ctx:SimpleLangParser.PreDecExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#printfExpr.
    def visitPrintfExpr(self, ctx:SimpleLangParser.PrintfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#callExpr.
    def visitCallExpr(self, ctx:SimpleLangParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#relExpr.
    def visitRelExpr(self, ctx:SimpleLangParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignExpr.
    def visitAssignExpr(self, ctx:SimpleLangParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:SimpleLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#argList.
    def visitArgList(self, ctx:SimpleLangParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#type.
    def visitType(self, ctx:SimpleLangParser.TypeContext):
        return self.visitChildren(ctx)



del SimpleLangParser