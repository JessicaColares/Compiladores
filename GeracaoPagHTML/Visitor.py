from HtmlParser import HtmlParser
from HtmlVisitor import HtmlVisitor

class HtmlOutput():
    
    def __init__(self):
        self.conteudo = "<!DOCTYPE html>\n<html>\n"
        self.conteudo += "<head>\n<meta charset='UTF-8'>\n"
        self.conteudo += "<title>Formulário Gerado</title>\n</head>\n"
        self.conteudo += "<body style='font-family: Arial, sans-serif; margin: 20px;'>\n"
        self.conteudo += "<form>\n"
        self.count = 0

    def addText(self, cols, rows, s):
        self.conteudo += f"<div style='margin-bottom: 15px;'>\n"
        self.conteudo += f"<label>{s}</label><br>\n"
        self.conteudo += f"<textarea name='Q{self.count}' cols='{cols}' rows='{rows}'"
        self.conteudo += " style='width: 300px; padding: 5px;'></textarea>\n"
        self.conteudo += "</div>\n\n"
        self.count += 1
    
    def addRadio(self, s, options):
        self.conteudo += f"<div style='margin-bottom: 15px;'>\n"
        self.conteudo += f"<label>{s}</label><br>\n"
        for val in options:
            self.conteudo += f"<input type='radio' name='Q{self.count}' value='{val}'"
            self.conteudo += f" style='margin: 5px;'> {val}<br>\n"
        self.conteudo += "</div>\n\n"
        self.count += 1
    
    def addCheckBox(self, s, options):
        self.conteudo += f"<div style='margin-bottom: 15px;'>\n"
        self.conteudo += f"<label>{s}</label><br>\n"
        for val in options: 
            self.conteudo += f"<input type='checkbox' name='Q{self.count}' value='{val}'"
            self.conteudo += f" style='margin: 5px;'> {val}<br>\n"
            self.count += 1
        self.conteudo += "</div>\n\n"

    def addMenu(self, id_menu, label, options):
        self.conteudo += f"<div style='margin-bottom: 15px;'>\n"
        self.conteudo += f"<label for='{id_menu}'>{label}</label><br>\n"
        self.conteudo += f"<select name='{id_menu}' id='{id_menu}' style='padding: 5px; width: 200px;'>\n"
        for value, text in options:
            self.conteudo += f"  <option value='{value}'>{text}</option>\n"
        self.conteudo += "</select>\n</div>\n\n"
        self.count += 1

    def addButton(self, label, alert_message):
        self.conteudo += f"<div style='margin-bottom: 15px;'>\n"
        self.conteudo += f"<button type='button' onclick=\"alert('{alert_message}')\""
        self.conteudo += " style='padding: 8px 15px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;'>"
        self.conteudo += f"{label}</button>\n</div>\n\n"
        self.count += 1

    def addTable(self, caption, headers, rows):
        self.conteudo += "<div style='margin-bottom: 20px;'>\n"
        self.conteudo += "<table style='border-collapse: collapse; width: 100%;'>\n"
        self.conteudo += f"  <caption style='font-weight: bold; margin-bottom: 10px;'>{caption}</caption>\n"
        
        # Cabeçalho
        self.conteudo += "  <tr style='background-color: #f2f2f2;'>\n"
        for header in headers:
            self.conteudo += f"    <th style='border: 1px solid #ddd; padding: 8px; text-align: left;'>{header}</th>\n"
        self.conteudo += "  </tr>\n"
        
        # Linhas
        for row in rows:
            self.conteudo += "  <tr>\n"
            for cell in row:
                self.conteudo += f"    <td style='border: 1px solid #ddd; padding: 8px;'>{cell}</td>\n"
            self.conteudo += "  </tr>\n"
        
        self.conteudo += "</table>\n</div>\n\n"
        self.count += 1

    def close(self):
        self.conteudo += "</form>\n"
        self.conteudo += "</body>\n"
        self.conteudo += "</html>\n"
        print(self.conteudo)

class Visitor(HtmlVisitor):

    def __init__(self):
        self.html = HtmlOutput()

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        for questao in l:
            self.visit(questao)
        self.html.close()
       
    def visitQTexto(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 4:
            cols = l[1].getText()
            rows = l[2].getText()
            string = self.visit(l[3])
            self.html.addText(cols, rows, string)

    def visitQRadioBox(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 3:
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addRadio(string, opcoes)
    
    def visitQCheckBox(self, ctx: HtmlParser.QCheckBoxContext):
        l = list(ctx.getChildren())
        if len(l) == 3:
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addCheckBox(string, opcoes)

    def visitQMenu(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 4:
            id_menu = self.visit(l[1])
            label = self.visit(l[2])
            options = self.visit(l[3])
            self.html.addMenu(id_menu, label, options)

    def visitQBotao(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 3:
            label = self.visit(l[1])
            alert_message = self.visit(l[2])
            self.html.addButton(label, alert_message)

    def visitQTabela(self, ctx):
        l = list(ctx.getChildren())
        if len(l) >= 3:
            caption = self.visit(l[1])
            headers = self.visit(l[2])
            rows = [self.visit(linha) for linha in l[3:]]
            self.html.addTable(caption, headers, rows)

    def visitOpcoes(self, ctx):
        opcoes = [self.visit(str_ctx) for str_ctx in ctx.str_()]
        return opcoes

    def visitOpcoesValores(self, ctx):
        return [self.visit(par) for par in ctx.parStrStr()]

    def visitCabecalho(self, ctx):
        return [self.visit(str_ctx) for str_ctx in ctx.str_()]

    def visitLinha(self, ctx):
        return [self.visit(str_ctx) for str_ctx in ctx.str_()]

    def visitParStrStr(self, ctx):
        return (self.visit(ctx.str_(0)), self.visit(ctx.str_(1)))

    def visitStr_(self, ctx):
        return ctx.getText().strip('"')