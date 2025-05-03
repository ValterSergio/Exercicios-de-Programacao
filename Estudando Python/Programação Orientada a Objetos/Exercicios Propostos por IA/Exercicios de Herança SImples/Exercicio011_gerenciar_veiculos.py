# Classe base, sendo generica para veiculso
class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, disponivel: bool):
        """
        Inicializa os atributos básicos de um veículo.

        Args:
            marca (str): Marca do veículo.
            modelo (str): Modelo do veículo.
            ano (int): Ano de fabricação.
            disponivel (bool): Status de disponibilidade.
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.disponivel = disponivel
    
    def alterar_disponibilidade(self) -> None:
        """Alterna o status de disponibilidade do veículo."""
        self.disponivel = not self.disponivel
    
    def exibir_dados(self) -> str:
        """Retorna uma string com os dados completos do veículo."""
        marca = f"Marca: {self.marca} "
        modelo = f"Modelo: {self.modelo} "
        ano = f"Ano: {self.ano} "
        disponivel = f"Disponibilidade: {'Disponível' if self.disponivel else 'Indisponível'}"
        return f"Dados do Veículo\n{marca}\n{modelo}\n{ano}\n{disponivel}"

# Classe derivada de Veiculo, específica para carros
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, disponivel: bool, nro_portas: int):
        """
        Inicializa os dados de um carro, herdando atributos de Veiculo.

        Args:
            nro_portas (int): Número de portas do carro.
        """
        super().__init__(marca, modelo, ano, disponivel)
        self.nro_portas = nro_portas
    
    def alterar_quantidade_portas(self, nova_quantidade):
        """
        Altera o número de portas do carro se estiver entre 2 e 4.

        Returns:
            bool: True se a alteração foi feita, False caso contrário.
        """
        if 2 <= nova_quantidade <= 4:
            self.nro_portas = nova_quantidade
            return True
        return False
    
    def exibir_dados(self):
        """Retorna os dados do carro incluindo o número de portas."""
        return f"{super().exibir_dados()}\nNúmero de Portas: {self.nro_portas}\n"


# Classe derivada de Veiculo, específica para motos
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, disponivel, tipo: str):
        """
        Inicializa os dados de uma moto.

        Args:
            tipo (str): Categoria da moto (ex: 'trabalho', 'passeio').
        """
        super().__init__(marca, modelo, ano, disponivel)
        self.tipo = tipo
    
    def alterar_tipo(self, novo: str) -> None:
        """Altera a categoria da moto."""
        self.tipo = novo

    def exibir_dados(self):
        """Retorna os dados da moto incluindo a categoria."""
        return f"{super().exibir_dados()}\nCategoria: {self.tipo}"


# Função para testar a classe Moto
def testar_classe_moto():
    print("Testando classe Moto - instanciando objeto")
    testar_classe_moto = Moto("Honda", "Titan 150", 2015, False, "trabalho")

    print("Testar o método exibir_dados()")
    testar_metodo_exibir_dados = testar_classe_moto.exibir_dados()

    print("Imprimindo o valor do método")
    print(testar_metodo_exibir_dados)
    print()

    print("Alterando o tipo da moto e a disponibilidade")
    testar_classe_moto.alterar_tipo("passeio")
    testar_classe_moto.alterar_disponibilidade()

    print("Confirmando as modificações com o método exibir_dados")
    testar_metodo_exibir_dados = testar_classe_moto.exibir_dados()
    print(testar_metodo_exibir_dados)


# Função para testar a classe Veiculo base
def testar_classe_veiculo():
    print("Testando classe Veiculo - instanciando objeto")
    teste_veiculo_base = Veiculo("Honda", "Civic", 2000, False)

    print("Obtendo dados pelo método exibir_dados")
    teste_dados_veiculo_base = teste_veiculo_base.exibir_dados()

    print("Exibindo a saída do método exibir_dados()")
    print(teste_dados_veiculo_base)
    print()

    print("Alterando a disponibilidade do veículo com o método alterar_disponibilidade()")
    teste_veiculo_base.alterar_disponibilidade()

    print("Confirmando funcionalidade com o método exibir_dados")
    teste_dados_veiculo_base = teste_veiculo_base.exibir_dados()

    print("Exibindo a saída do método exibir_dados()")
    print(teste_dados_veiculo_base)
    print()


# Função para testar a classe Carro
def testar_classe_carro():
    print()
    print("Testando a classe Carro - instanciando objeto")
    teste_carro = Carro("Renault", "Clio V6", 2005, True, 2)

    print("Testando o método exibir_dados")
    teste_exibir_dados_carro = teste_carro.exibir_dados()

    print("Exibindo os dados do carro")
    print(teste_exibir_dados_carro)
    print()

    print("Testando método alterar número de portas")
    teste_carro.alterar_quantidade_portas(4)

    print("Chamando o método da classe pai - alterar_disponibilidade()")
    teste_carro.alterar_disponibilidade()

    print("Testando o método exibir_dados novamente")
    teste_exibir_dados_carro = teste_carro.exibir_dados()

    print("Exibindo os dados do carro para confirmar alterações")
    print(teste_exibir_dados_carro)
    print()


# Execução principal
if __name__ == "__main__":
    testar_classe_veiculo()
    testar_classe_carro()
    testar_classe_moto()
