"""
Composição com Injeção de Dependência

Cenário: Um EditorDeTexto recebe uma Fonte como parâmetro. Você pode trocar a fonte sem mudar o editor.
"""

class Fonte:
    def __init__(self, nome):
        self.nome = nome

class EditorDeTexto:
    def __init__(self, fonte):
        self.fonte = fonte

    def imprimir_config(self):
        return f"Usando a fonte: {self.fonte.nome}"

fonte = Fonte("XLR8")
editor = EditorDeTexto(fonte)
print(editor.imprimir_config())