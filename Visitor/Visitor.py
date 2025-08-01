from ExprVisitor import ExprVisitor
import math

class Visitor(ExprVisitor):
    def visitRoot(self, ctx):
        return self.visit(ctx.expr())
    
    def visitParent(self, ctx):
        return self.visit(ctx.expr())
    
    def visitPot(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right
    
    def visitMultDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left * right if op == '*' else left / right
    
    def visitSomaSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return left + right if op == '+' else left - right
    
    def visitFunc(self, ctx):
        if ctx.abs_():
            return self.visit(ctx.abs_())
        else:
            return self.visit(ctx.fact())
    
    def visitAbs_(self, ctx):
        return abs(self.visit(ctx.expr()))
    
    def visitFact(self, ctx):
        value = self.visit(ctx.expr())
        if value < 0 or value != int(value):
            raise ValueError("Fatorial só pode ser aplicado a inteiros não negativos")
        return float(math.factorial(int(value)))
    
    def visitNumber(self, ctx):
        num_text = ctx.NUM().getText()
        if ctx.getChild(0).getText() == '-':
            num_text = '-' + num_text
        return float(num_text)