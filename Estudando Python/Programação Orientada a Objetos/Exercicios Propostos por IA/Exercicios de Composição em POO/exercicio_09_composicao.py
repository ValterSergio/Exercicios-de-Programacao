class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f"{self.nome} - R${self.preco}"

class ProdutoFisico(Produto):
    def calcular_frete(self, peso_kg: float) -> float:
        return peso_kg * 10  # R$10 por kg

class ProdutoDigital(Produto):
    def gerar_link_download(self) -> str:
        return f"https://meusite.com/download/{self.nome.replace(' ', '_')}"

class ProdutoAssinatura(Produto):
    def renovar(self) -> str:
        return "Assinatura renovada com sucesso!"

class Cliente:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

class Pagamento:
    def __init__(self, valor: float, metodo: str):
        self.valor = valor
        self.metodo = metodo

    def processar_pagamento(self):
        return f"Pagamento de R${self.valor} via {self.metodo} realizado!"

class Pedido:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.produtos = []
        self.pagamento = None

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def fechar_pedido(self, metodo_pagamento: str):
        total = sum(produto.preco for produto in self.produtos)
        self.pagamento = Pagamento(total, metodo_pagamento)
        return self.pagamento.processar_pagamento()

if __name__ == "__main__":
    # Criando cliente
    cliente1 = Cliente("Ana Souza", "ana@example.com")

    # Criando produtos
    livro = ProdutoFisico("Livro Python", 50.0)
    curso = ProdutoDigital("Curso de Django", 120.0)
    assinatura = ProdutoAssinatura("Clube de Livros", 30.0)

    # Criando pedido
    pedido = Pedido(cliente1)
    pedido.adicionar_produto(livro)
    pedido.adicionar_produto(curso)
    pedido.adicionar_produto(assinatura)

    # Fechando pedido
    print(pedido.fechar_pedido("Cartão de Crédito"))

    # Testando métodos específicos
    print(f"Descrição do produto físico: {livro.descricao()}")
    print(f"Frete do livro (2kg): R${livro.calcular_frete(2)}")
    print(f"Link para download do curso: {curso.gerar_link_download()}")
    print(f"Status da assinatura: {assinatura.renovar()}")
