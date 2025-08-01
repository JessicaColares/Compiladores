# Generated from SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#prog.
    def visitProg(self, ctx:SimpleLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#function.
    def visitFunction(self, ctx:SimpleLangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifStatement.
    def visitIfStatement(self, ctx:SimpleLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#whileStatement.
    def visitWhileStatement(self, ctx:SimpleLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#declaration.
    def visitDeclaration(self, ctx:SimpleLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignment.
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#returnStatement.
    def visitReturnStatement(self, ctx:SimpleLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#block.
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#expression.
    def visitExpression(self, ctx:SimpleLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#logicalOr.
    def visitLogicalOr(self, ctx:SimpleLangParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#logicalAnd.
    def visitLogicalAnd(self, ctx:SimpleLangParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#equality.
    def visitEquality(self, ctx:SimpleLangParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#relational.
    def visitRelational(self, ctx:SimpleLangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#additive.
    def visitAdditive(self, ctx:SimpleLangParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#multiplicative.
    def visitMultiplicative(self, ctx:SimpleLangParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#unary.
    def visitUnary(self, ctx:SimpleLangParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#primary.
    def visitPrimary(self, ctx:SimpleLangParser.PrimaryContext):
        return self.visitChildren(ctx)



del SimpleLangParser