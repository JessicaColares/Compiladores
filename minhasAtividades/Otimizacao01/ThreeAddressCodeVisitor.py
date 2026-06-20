# Generated from ThreeAddressCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ThreeAddressCodeParser import ThreeAddressCodeParser
else:
    from ThreeAddressCodeParser import ThreeAddressCodeParser

# This class defines a complete generic visitor for a parse tree produced by ThreeAddressCodeParser.

class ThreeAddressCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ThreeAddressCodeParser#program.
    def visitProgram(self, ctx:ThreeAddressCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#line.
    def visitLine(self, ctx:ThreeAddressCodeParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#assignment.
    def visitAssignment(self, ctx:ThreeAddressCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ThreeAddressCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#label.
    def visitLabel(self, ctx:ThreeAddressCodeParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#goto.
    def visitGoto(self, ctx:ThreeAddressCodeParser.GotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#binaryExpr.
    def visitBinaryExpr(self, ctx:ThreeAddressCodeParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#id.
    def visitId(self, ctx:ThreeAddressCodeParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ThreeAddressCodeParser#int.
    def visitInt(self, ctx:ThreeAddressCodeParser.IntContext):
        return self.visitChildren(ctx)



del ThreeAddressCodeParser