class Departamento:
    """
    Representa um departamento dentro da empresa.

    Cada departamento possui um setor (nome) e uma lista de funcionários
    que pertencem a ele. Permite adicionar novos funcionários e listar os
    que já estão cadastrados.
    """

    def __init__(self, setor: str):
        """
        Inicializa uma instância do departamento com um nome de setor.

        Args:
            setor (str): Nome do setor/departamento (ex: "T.I", "RH").
        """
        self.setor = setor
        self.lista_funcionarios = []  # Lista para armazenar os funcionários do departamento

    def adicionar_funcionario(self, funcionario: object):
        """
        Adiciona um funcionário à lista de funcionários do departamento.

        Args:
            funcionario (object): Instância da classe Funcionario a ser adicionada.
        """
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        """
        Exibe todos os funcionários cadastrados no departamento.

        Para cada funcionário, exibe nome e cargo, formatado com separadores.
        """
        print("-" * 65)
        print(f"Profissionais do setor de {self.setor}")
        print("-" * 65)
        
        for funcionario in self.lista_funcionarios:
            print("Nome: ", funcionario.get_nome())
            print("Cargo: ", funcionario.get_cargo())
            print("-" * 65)
