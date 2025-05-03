class Item:
    def __init__(self, nome: str, valor: float):
        self.nome = nome
        self.valor = valor
    
    def exibir_pedido(self):
        return f"Item: {self.nome} | Preço: {self.valor}"

class PedidoSimples:
    def __init__(self, bebida: str, preco_bebida: float, comida: str, preco_comida: float):
        self.pedido_bebida = Item(bebida, preco_bebida)
        self.pedido_comida = Item(comida, preco_comida)
    
    def exibir_pedido(self):
        print("Bebidas")
        print(self.pedido_bebida.exibir_pedido(), '\n')
        print("Comidas")
        print(self.pedido_comida.exibir_pedido(), '\n')
    
class PedidoMontado:
    def __init__(self, lista: list[Item]):
        self.lista = lista
    
    def calcular_total_da_compra(self):
        total = 0
        for compra in self.lista:
            total += compra.valor
        return total
    
    def exibir_compra(self):
        print("-"*65)
        print("Produtos No Carrinho")
        print("-"*65)
        for item in self.lista:
            print(item.exibir_pedido())
        print(f"Total da Compra: R$ {self.calcular_total_da_compra():,.2f}")
        print("-"*65)

class PedidoDinamico:
    def __init__(self):
        self.lista = []
    
    def adicionar_item(self, nome: str, preco: float):
        self.lista.append(Item(nome, preco))
    
    def remover_item(self, nome: str):
        lista_nova = []
        for item in self.lista:
            if item.nome != nome:
                lista_nova.append(item)
        
        self.lista = lista_nova
    
    def exibir_pedido(self):
        pedido = PedidoMontado(self.lista)
        pedido.exibir_compra()

if __name__ == "__main__":
    # Teste da classe Item
    print("Teste da classe Item")
    item1 = Item("Refrigerante", 5.0)
    print(item1.exibir_pedido())
    print()

    # Teste da classe PedidoSimples
    print("Teste da classe PedidoSimples")
    pedido_simples = PedidoSimples("Suco", 4.5, "Salgado", 6.5)
    pedido_simples.exibir_pedido()
    print()

    # Teste da classe PedidoMontado
    print("Teste da classe PedidoMontado")
    itens = [
        Item("Hambúrguer", 12.0),
        Item("Batata Frita", 8.0),
        Item("Refrigerante", 5.0)
    ]
    pedido_montado = PedidoMontado(itens)
    pedido_montado.exibir_compra()
    print()

    # Teste da classe PedidoDinamico
    print("Teste da classe PedidoDinamico")
    pedido_dinamico = PedidoDinamico()
    pedido_dinamico.adicionar_item("Pizza", 20.0)
    pedido_dinamico.adicionar_item("Cerveja", 7.0)
    pedido_dinamico.adicionar_item("Água", 3.0)

    print("Antes de remover item:")
    pedido_dinamico.exibir_pedido()

    # Tentando remover "Cerveja"
    pedido_dinamico.remover_item("Cerveja")
    print("\nDepois de tentar remover 'Cerveja':")
    pedido_dinamico.exibir_pedido()
