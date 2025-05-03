"""Composição Simples com Instanciação Direta"""

"""
Cenário: Um Livro é composto por várias Páginas. As páginas não existem fora do livro.
"""

class Pagina:
    def __init__(self, numero: int, conteudo: str):
        self.numero = numero
        self.conteudo = conteudo
    
    def exibir(self):
        return f"Página: {self.numero} | Conteudo: {self.conteudo}"

class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.paginas = [Pagina(1, "Olá "), Pagina(2, "Mundo"), Pagina(3, " !!!")]

    def mostrar_paginas(self):
        return "\n".join(x.exibir() for x in self.paginas)
        

livro = Livro("João e o Pé de feijão")
print(livro.mostrar_paginas())