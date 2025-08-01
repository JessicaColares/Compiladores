from ExprListener import ExprListener

class Listener(ExprListener):
    def __init__(self):
        self.stack = []
    
    def get_result(self):
        return self.stack.pop()
    
    def exitNumber(self, ctx):
        num_text = ctx.NUM().getText()
        if ctx.getChild(0).getText() == '-':
            num_text = '-' + num_text
        num = float(num_text)
        self.stack.append(num)
    
    def exitParent(self, ctx):
        pass  # Valor já está na pilha
    
    def exitPot(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        self.stack.append(left ** right)
    
    def exitMultDiv(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(left * right if op == '*' else left / right)
    
    def exitSomaSub(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(left + right if op == '+' else left - right)
    
    def exitAbs_(self, ctx):
        self.stack.append(abs(self.stack.pop()))
    
    def exitFact(self, ctx):
        value = self.stack.pop()
        if value < 0 or value != int(value):
            raise ValueError("Fatorial só pode ser aplicado a inteiros não negativos")
        self.stack.append(float(math.factorial(int(value))))

import math  