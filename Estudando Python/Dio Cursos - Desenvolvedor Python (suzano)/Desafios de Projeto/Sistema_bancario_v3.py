from abc import ABC, abstractmethod
from datetime import datetime

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento: str):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def get_nome(self) -> str:
        return self.nome
    
    def get_cpf(self) -> str:
        return self.cpf
    
    def get_data_nascimento(self) -> str:
        return self.data_nascimento
    
    def set_nome(self, novo_nome: str) -> bool:
        erro = False

        if novo_nome == f'{novo_nome[0]}' * len(novo_nome):
            print("Erro: letras repetem em execesso")
            erro = True
            

        if len(novo_nome) <= 2:
            print("Erro: nome muito curto")
            erro = True
        
        if any([char for char in novo_nome if char.isnumeric()]):
            print("Erro: Não pode haver números no nome")
            erro = True

        if erro: return False
        self.nome = novo_nome
        print("Nome alterado com sucesso")
        return True        
    
    def set_cpf(self, novo_cpf: str) -> bool:
        erro = False

        if len(novo_cpf) != 11:
            print("Erro: CPF invalido")
            erro = True
            
        if novo_cpf == f'{novo_cpf[0]}' * len(novo_cpf):
            print("Erro: todos os numeros são iguais")
            erro = True
        
        if erro: return False
        self.cpf = novo_cpf
        print("CPF alterado com sucesso")
        return True
    
    def set_data_nascimento(self, nova_data: str) -> bool:
        self.data_nascimento = nova_data
        return True

class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, endereco: str):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta: object, transacao: object):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta: object):
        self.contas.append(conta)
    

    def get_endereco(self) -> str:
        return self.endereco
    
    def set_endereco(self, novo_endereco) -> bool:
        self.endereco = novo_endereco
        return True
    
class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def get_transacoes(self) -> list:
        return self.transacoes

class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    def get_saldo(self) -> float:
        return self._saldo
    
    def set_saldo(self, novo_saldo: float) -> bool:
        # novo saldo deve ser sempre maior que zero
        saldo_positivo = novo_saldo >= 0
        if not saldo_positivo:
            print("Erro: Saldo não pode ficar negativo")
            return False
        
        self._saldo = novo_saldo
        return True

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(numero, cliente)
    
    def get_numero_agencia(self) -> str:
        return self._agencia
    
    def get_cliente(self) -> Cliente:
        return self._cliente
    
    def get_historico(self) -> Historico:
        return self._historico
    
    def sacar(self, valor: float) -> bool:
        if valor > self.get_saldo():
            print("Erro: Saldo insuficiente")
            return False
        
        calcular_saldo = -1
        if not valor > 0:
            print("Erro: Valor de Saque deve ser positivo")
            return False
        
        calcular_saldo = self.get_saldo() - valor
        saldo_alterado = self.set_saldo(calcular_saldo)

        if not saldo_alterado:
            print("Erro: Cliente não pode ficar negativado")
            return False

        return True 

    def depositar(self, valor: float) -> bool:
        isnumber = isinstance(valor, float|int)
        if not isnumber:
            print("Digite um número válido")
            return False
        
        if not valor > 0:
            print("Erro: Valor para Deposito deve ser positivo")
            return False
        
        calcular_saldo = self.get_saldo() + valor
        return self.set_saldo(calcular_saldo)
    
class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite: int=500, limite_saques: int=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor: float) -> bool:
        numero_saques = len([
        transacao for transacao in self.get_historico().get_transacoes()
        if isinstance(transacao, Saque)
        ])

        
        passou_limite = valor > self.limite

        if passou_limite:
            print("Erro: Valor de saque passou do limite permitido")
            return False

        if numero_saques >= self.limite_saques:
            print("Erro: Limite de Saques Esgotado")
            return False
        
        if super().sacar(valor):
            return True
        
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Transacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.get_historico().adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.get_historico().adicionar_transacao(self)

if __name__ == "__main__":
    print("==== INICIANDO TESTES ====")

    # Criando os clientes
    cliente1 = Cliente("12345678900", "Alice", "1990-01-01", "Rua A, 123")
    cliente2 = Cliente("22233344455", "Bruno", "1985-05-15", "Av. B, 456")
    cliente3 = Cliente("98765432100", "Carla", "2000-10-30", "Rua C, 789")

    print("\n--- Clientes Criados ---")
    print(cliente1.get_nome(), cliente1.get_cpf())
    print(cliente2.get_nome(), cliente2.get_cpf())
    print(cliente3.get_nome(), cliente3.get_cpf())

    # Criando contas para os clientes
    conta1 = ContaCorrente.nova_conta(cliente1, 1)
    conta2 = ContaCorrente.nova_conta(cliente2, 2)
    conta3 = ContaCorrente.nova_conta(cliente3, 3)

    # Adicionando contas aos clientes
    cliente1.adicionar_conta(conta1)
    cliente2.adicionar_conta(conta2)
    cliente3.adicionar_conta(conta3)

    print("\n--- Contas Criadas ---")
    print(conta1.get_cliente().get_nome(), "- Conta Nº:", conta1._numero)
    print(conta2.get_cliente().get_nome(), "- Conta Nº:", conta2._numero)
    print(conta3.get_cliente().get_nome(), "- Conta Nº:", conta3._numero)

    # Testes de transações
    print("\n--- Transações Cliente 1 ---")
    cliente1.realizar_transacao(conta1, Deposito(1000))   # sucesso
    cliente1.realizar_transacao(conta1, Deposito(-50))    # erro
    cliente1.realizar_transacao(conta1, Saque(200))       # sucesso
    cliente1.realizar_transacao(conta1, Saque(1000))      # erro: saldo insuficiente
    cliente1.realizar_transacao(conta1, Saque(-10))       # erro: valor negativo

    print("\n--- Saldo Final Cliente 1 ---")
    print("Saldo:", conta1.get_saldo())

    print("\n--- Transações Cliente 2 ---")
    cliente2.realizar_transacao(conta2, Deposito(500))    # sucesso
    cliente2.realizar_transacao(conta2, Saque(600))       # erro: acima do limite
    cliente2.realizar_transacao(conta2, Saque(400))       # sucesso
    cliente2.realizar_transacao(conta2, Saque(50))        # sucesso
    cliente2.realizar_transacao(conta2, Saque(20))        # sucesso
    cliente2.realizar_transacao(conta2, Saque(10))        # erro: limite de saques

    print("\n--- Saldo Final Cliente 2 ---")
    print("Saldo:", conta2.get_saldo())

    print("\n--- Transações Cliente 3 ---")
    cliente3.realizar_transacao(conta3, Deposito(300))    # sucesso
    cliente3.realizar_transacao(conta3, Deposito("cem"))  # erro: tipo errado (vai quebrar)
    cliente3.realizar_transacao(conta3, Saque(100))       # sucesso

    print("\n--- Saldo Final Cliente 3 ---")
    print("Saldo:", conta3.get_saldo())

    print("\n==== FIM DOS TESTES ====")
