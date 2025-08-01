from antlr4 import *
from miniCVisitor import miniCVisitor

class SemanticVisitor(miniCVisitor):
    def __init__(self):
        super().__init__()
        self.symbol_table = {
            'variables': {},
            'functions': {},
            'current_scope': 'global'
        }
        self.errors = []
        self.scope_stack = []
        self.loop_depth = 0
    
    def add_error(self, message, ctx):
        token = ctx.start
        # Verifica se o erro já foi reportado para esta linha/coluna
        existing_error = next((e for e in self.errors 
                             if f"linha {token.line}:{token.column}" in e), None)
        if not existing_error:
            self.errors.append(f"Erro semântico na linha {token.line}:{token.column} - {message}")
    
    # Adicionando tratamento explícito para comentários
    def visitComment(self, ctx):
        return None  # Ignora completamente os nós de comentário
    
    def visitProgram(self, ctx):
        self.symbol_table['variables']['global'] = {}
        self.visitChildren(ctx)
        return None
    
    def visitFunction_definition(self, ctx):
        func_name = ctx.function_header().IDENTIFIER().getText()
        return_type = ctx.type_().getText() if ctx.type_() else 'void'
        
        params = []
        if ctx.function_header().parameter_list():
            for param in ctx.function_header().parameter_list().parameter_declaration():
                param_type = param.type_().getText()
                param_name = param.declarator().IDENTIFIER().getText()
                params.append({'name': param_name, 'type': param_type})
        
        self.symbol_table['functions'][func_name] = {
            'return_type': return_type,
            'params': params
        }
        
        self.scope_stack.append(self.symbol_table['current_scope'])
        self.symbol_table['current_scope'] = func_name
        self.symbol_table['variables'][func_name] = {}
        
        for param in params:
            self.symbol_table['variables'][func_name][param['name']] = param['type']
        
        self.visit(ctx.function_body())
        
        self.symbol_table['current_scope'] = self.scope_stack.pop()
        return None
    
    def visitBlock(self, ctx):
        previous_scope = self.symbol_table['current_scope']
        new_scope = f"{previous_scope}_block_{id(ctx)}"
        
        self.scope_stack.append(previous_scope)
        self.symbol_table['current_scope'] = new_scope
        self.symbol_table['variables'][new_scope] = {}
        
        self.visitChildren(ctx)
        
        self.symbol_table['current_scope'] = self.scope_stack.pop()
        return None
    
    def visitData_definition(self, ctx):
        var_type = ctx.type_().getText()
    
        for declarator in ctx.declarator():
            var_name = declarator.IDENTIFIER().getText()
        
            if var_name in self.symbol_table['variables'].get(self.symbol_table['current_scope'], {}):
                self.add_error(f"Variável '{var_name}' já declarada neste escopo", declarator)
                continue
            
            if self.symbol_table['current_scope'] not in self.symbol_table['variables']:
                self.symbol_table['variables'][self.symbol_table['current_scope']] = {}
            
            self.symbol_table['variables'][self.symbol_table['current_scope']][var_name] = var_type
        
            if declarator.expression():
                expr_type = self.visit(declarator.expression())
                if expr_type and expr_type != var_type:
                    self.add_error(
                        f"Tipo incompatível na inicialização. Esperado: {var_type}, obtido: {expr_type}",
                        declarator.expression()
                    )
        return None
    
    def visitFunction_call(self, ctx):
        func_name = ctx.IDENTIFIER().getText()
        
        if func_name not in self.symbol_table['functions']:
            self.add_error(f"Função '{func_name}' não declarada", ctx)
            return None
        
        func_info = self.symbol_table['functions'][func_name]
        args = ctx.argument_list().expression() if ctx.argument_list() else []
        
        # Verifica número de argumentos
        if len(args) != len(func_info['params']):
            self.add_error(
                f"Número incorreto de argumentos para '{func_name}'. Esperados: {len(func_info['params'])}, fornecidos: {len(args)}",
                ctx
            )
        
        # Verifica tipos dos argumentos (só se o número estiver correto)
        if len(args) == len(func_info['params']):
            for i, (arg, param) in enumerate(zip(args, func_info['params'])):
                arg_type = self.visit(arg)
                if arg_type and arg_type != param['type']:
                    self.add_error(
                        f"Tipo incorreto para argumento {i+1} de '{func_name}'. Esperado: {param['type']}, fornecido: {arg_type}",
                        arg
                    )
        
        return func_info['return_type']
    
    def visitPrimary(self, ctx):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            
            # Verifica todos os escopos acessíveis
            for scope in [self.symbol_table['current_scope']] + self.scope_stack + ['global']:
                if var_name in self.symbol_table['variables'].get(scope, {}):
                    return self.symbol_table['variables'][scope][var_name]
            
            # Verifica se é função
            if var_name in self.symbol_table['functions']:
                return self.symbol_table['functions'][var_name]['return_type']
            
            self.add_error(f"Identificador '{var_name}' não declarado", ctx)
            return None
            
        elif ctx.CONSTANT_INT():
            return 'int'
        elif ctx.CONSTANT_CHAR():
            return 'char'
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None
    
    def visitBinary(self, ctx):
        # Atribuições
        if ctx.IDENTIFIER() and ctx.getChild(1).getText() in ['=', '+=', '-=', '*=', '/=', '%=']:
            var_name = ctx.IDENTIFIER().getText()
            var_type = None
            
            # Busca em todos os escopos
            for scope in [self.symbol_table['current_scope']] + self.scope_stack + ['global']:
                if var_name in self.symbol_table['variables'].get(scope, {}):
                    var_type = self.symbol_table['variables'][scope][var_name]
                    break
            
            if not var_type:
                self.add_error(f"Variável '{var_name}' não declarada", ctx)
                return None
            
            expr_type = self.visit(ctx.binary(0))
            if expr_type:
                # Operações compostas só para int
                if ctx.getChild(1).getText() != '=' and var_type != 'int':
                    self.add_error(
                        f"Operação '{ctx.getChild(1).getText()}' só é permitida para inteiros", 
                        ctx
                    )
                elif expr_type != var_type:
                    self.add_error(
                        f"Tipos incompatíveis na atribuição. Esperado: {var_type}, fornecido: {expr_type}",
                        ctx
                    )
            
            return var_type
        
        # Operações aritméticas
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/', '%']:
            left_type = self.visit(ctx.binary(0))
            right_type = self.visit(ctx.binary(1))
            
            if left_type and right_type:
                # Só + permite tipos diferentes (char+char ou int+int)
                if ctx.getChild(1).getText() == '+':
                    if left_type != right_type:
                        self.add_error("Operação '+' requer operandos do mesmo tipo", ctx)
                else:
                    if left_type != 'int' or right_type != 'int':
                        self.add_error(f"Operação '{ctx.getChild(1).getText()}' requer operandos do tipo 'int'", ctx)
                
                return left_type if left_type == right_type else None
        
        return self.visitChildren(ctx)
    
    def visitWhile_statement(self, ctx):
        self.loop_depth += 1
        cond_type = self.visit(ctx.expression())
        if cond_type and cond_type != 'int':
            self.add_error("Condição do while deve ser do tipo 'int'", ctx.expression())
        self.visit(ctx.statement())
        self.loop_depth -= 1
        return None
    
    def visitIf_statement(self, ctx):
        cond_type = self.visit(ctx.expression())
        if cond_type and cond_type != 'int':
            self.add_error("Condição do if deve ser do tipo 'int'", ctx.expression())
        self.visit(ctx.statement(0))
        if ctx.ELSE():
            self.visit(ctx.statement(1))
        return None
    
    def visitBreak_statement(self, ctx):
        if self.loop_depth <= 0:
            self.add_error("Comando 'break' fora de um loop", ctx)
        return None
    
    def visitContinue_statement(self, ctx):
        if self.loop_depth <= 0:
            self.add_error("Comando 'continue' fora de um loop", ctx)
        return None