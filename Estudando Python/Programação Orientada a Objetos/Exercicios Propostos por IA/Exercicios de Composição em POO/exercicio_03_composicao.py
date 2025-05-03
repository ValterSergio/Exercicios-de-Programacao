"""
Composição com Múltiplos Objetos (Lista)
Cenário: Um CarrinhoDeCompras é composto por vários Items.
"""

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f"{self.nome} - R${self.preco:.2f}"

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def total(self):
        return sum(item.preco for item in self.itens)

    def listar_itens(self):
        return "\n".join(item.descricao() for item in self.itens)

arroz = Item("Arroz da vô", 32.65)
feijao = Item("Feijão da vô", 22.65)
ovo = Item("Ovo da Granja", 27.65)

cart = CarrinhoDeCompras()
cart.adicionar_item(arroz)
cart.adicionar_item(feijao)
cart.adicionar_item(ovo)

print(cart.listar_itens())
print(cart.total())