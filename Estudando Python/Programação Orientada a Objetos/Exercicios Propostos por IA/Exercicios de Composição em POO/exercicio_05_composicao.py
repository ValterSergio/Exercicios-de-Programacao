NUMERO_DE_PEDIDOS = 1

class Prato:
    def __init__(self, nome: str, ingredientes: list[str], valor: float):
        self.nome = nome
        self.ingredientes = ingredientes
        self.valor = valor

class Cardapio:
    def __init__(self):
        # Composição por instanciação direta
        self.pratos = [
            Prato("Feijoada", ["Feijão", "Carne de Porco", "Linguiça"], 47.85),
            Prato("Arroz", ["Arroz", "Alho", "Salsa", "Cebola"], 29.50),
            Prato("Bisteca", ["Alho", "Carne de Porco"], 15.56)
        ]
    
    def listar_pratos(self):
        for prato in self.pratos:
            print(f'Prato: {prato.nome}      valor: {prato.valor}')

class Mesa:
    def __init__(self, numero: int, capacidade: int=4):
        self.numero = numero
        self.capacidade = capacidade
        self.ocupada = False

class Garcom:
    def __init__(self, lista_mesas: list[Mesa], nome: str, turno: str):
        self.lista_mesas = lista_mesas
        self.nome = nome
    
    def atender_mesa(self, numero: int):
        for mesa in self.lista_mesas:
            if mesa.numero == numero:
                mesa.ocupada = True
                print("Mesa sendo atendida pelo ", self.nome.capitalize())

    def liberar_mesa(self, numero: int):
        for mesa in self.lista_mesas:
            if mesa.numero == numero:
                mesa.ocupada = False
    
    def exibir_mesas_atendidas(self):
        print("-"*65)
        print(f"Mesas Atendidas pelo {self.nome.capitalize()}")
        print("-"*65)
        for mesa in self.lista_mesas:
            if mesa.ocupada:
                print(f"Mesa: {mesa.numero}")
        print("\t\t----- FIM -----")
        print("-"*65)

class Pedido:

    def __init__(self, mesa: Mesa, cardapio: Cardapio):
        self.mesa = mesa
        self.cardapio = cardapio
        self.itens = []
    
    def adicionar_pedido(self, nome: str):
        for prato in self.cardapio.pratos:
            if prato.nome == nome:
                self.itens.append(prato)

    def remover_pedido(self, nome: str):
        for prato in self.cardapio.pratos:
            if prato.nome == nome:
                self.itens.remove(prato)

        
    
    def valor_total(self):
        return sum([x.valor for x in self.itens])
    
    def exibir_pedido(self):
        print(f"Mesa: {self.mesa.numero}")
        for prato in self.itens:
            print(f"- {prato.nome}")
        print(f"Total: R$ {self.valor_total():.2f}")


if __name__ == "__main__":
    cardapio = Cardapio()
    mesas = [Mesa(1), Mesa(2), Mesa(3)]

    garcom = Garcom(mesas, "Garçom", "Tarde/Noite")
    garcom.atender_mesa(2)

    pedido1 = Pedido(mesas[1], cardapio)
    cardapio.listar_pratos()

    pedido1.adicionar_pedido("Feijoada")
    pedido1.adicionar_pedido("Bisteca")
    pedido1.exibir_pedido()

    pedido1.remover_pedido("Bisteca")
    pedido1.exibir_pedido()

    garcom.exibir_mesas_atendidas()
    garcom.liberar_mesa(2)
    garcom.exibir_mesas_atendidas()
    