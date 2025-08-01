# Generated from miniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .miniCParser import miniCParser
else:
    from miniCParser import miniCParser

# This class defines a complete generic visitor for a parse tree produced by miniCParser.

class miniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniCParser#program.
    def visitProgram(self, ctx:miniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#definition.
    def visitDefinition(self, ctx:miniCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#data_definition.
    def visitData_definition(self, ctx:miniCParser.Data_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#type.
    def visitType(self, ctx:miniCParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#declarator.
    def visitDeclarator(self, ctx:miniCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#function_definition.
    def visitFunction_definition(self, ctx:miniCParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#function_header.
    def visitFunction_header(self, ctx:miniCParser.Function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#parameter_list.
    def visitParameter_list(self, ctx:miniCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:miniCParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#function_body.
    def visitFunction_body(self, ctx:miniCParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#block.
    def visitBlock(self, ctx:miniCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#statement.
    def visitStatement(self, ctx:miniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#expression.
    def visitExpression(self, ctx:miniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#binary.
    def visitBinary(self, ctx:miniCParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#unary.
    def visitUnary(self, ctx:miniCParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#primary.
    def visitPrimary(self, ctx:miniCParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniCParser#argument_list.
    def visitArgument_list(self, ctx:miniCParser.Argument_listContext):
        return self.visitChildren(ctx)



del miniCParser