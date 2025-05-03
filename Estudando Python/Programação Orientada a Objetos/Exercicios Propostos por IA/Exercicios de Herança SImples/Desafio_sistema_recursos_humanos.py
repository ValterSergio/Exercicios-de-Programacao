"""
Este código demonstra os principais conceitos de Programação Orientada a Objetos (POO):

1. **Encapsulamento**: Atributos e métodos privados com prefixo `_` ou `__`, e uso de getters e setters.
2. **Herança**: Classes como `Funcionario`, `Freelancer` e `Gerente` herdam da classe base `Colaborador`.
3. **Polimorfismo**: O método `exibir_detalhes` é redefinido em subclasses, comportando-se de forma diferente.
4. **Abstração**: A classe `Colaborador` fornece uma interface genérica para diferentes tipos de trabalhadores.
5. **Composição**: A classe `Gerente` herda múltiplas funcionalidades de `Funcionario` e `Comissao`.
"""

class Colaborador:
    """Classe base que representa um colaborador da empresa."""

    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def calcular_pagamento(self):
        """Deve ser sobrescrito nas subclasses, se necessário."""
        return 0

    def exibir_detalhes(self):
        """Deve ser sobrescrito nas subclasses."""
        print(f"{self.__class__.__name__} - Nome: {self.get_nome()} | Pagamento: Não definido")


class Funcionario(Colaborador):
    """Representa um funcionário com salário fixo."""

    def __init__(self, nome, salario):
        super().__init__(nome)
        self._salario = salario

    def get_salario(self):
        return self._salario

    def set_salario(self, novo_salario):
        if novo_salario > 0:
            self._salario = novo_salario
        else:
            print(f"Erro: salário inválido ({novo_salario}). Deve ser maior que zero.")

    def calcular_pagamento(self):
        return self.get_salario()

    def exibir_detalhes(self):
        print(f"Funcionario - Nome: {self.get_nome()} | Pagamento: R$ {self.calcular_pagamento():,.2f}")


class Freelancer(Colaborador):
    """Representa um freelancer que é pago por hora."""

    def __init__(self, nome, valor_hora):
        super().__init__(nome)
        self._valor_hora = valor_hora
        self._horas_trabalhadas = 0

    def get_valor_hora(self):
        return self._valor_hora

    def set_valor_hora(self, novo_valor):
        if novo_valor > 0:
            self._valor_hora = novo_valor
        else:
            print(f"Erro: valor da hora inválido ({novo_valor}). Deve ser maior que zero.")

    def set_horas_trabalhadas(self, horas):
        if horas > 0:
            self._horas_trabalhadas = horas
        else:
            print(f"Erro: horas trabalhadas inválidas ({horas})")

    def calcular_pagamento(self):
        return self._valor_hora * self._horas_trabalhadas

    def exibir_detalhes(self):
        print(f"Freelancer - Nome: {self.get_nome()} | Pagamento: R$ {self.calcular_pagamento():,.2f}")


class Comissao:
    """Classe auxiliar para representar comissão sobre vendas."""

    def __init__(self, comissao):
        self._comissao = comissao

    def get_comissao(self):
        return self._comissao

    def set_comissao(self, nova_comissao):
        self._comissao = nova_comissao

    def calcular_comissao(self, valor_vendas):
        if valor_vendas >= 0:
            return self.get_comissao() * valor_vendas
        else:
            print(f"Erro: valor de vendas inválido ({valor_vendas}). Deve ser >= 0.")
            return 0


class Gerente(Funcionario, Comissao):
    """Representa um gerente com salário fixo e comissão sobre vendas."""

    def __init__(self, nome, salario, comissao):
        Funcionario.__init__(self, nome, salario)
        Comissao.__init__(self, comissao)
        self._valor_vendas = 0

    def set_vendas(self, valor):
        if valor >= 0:
            self._valor_vendas = valor
        else:
            print(f"Erro: valor de vendas inválido ({valor}).")

    def calcular_pagamento(self):
        return self.get_salario() + self.calcular_comissao(self._valor_vendas)

    def exibir_detalhes(self):
        print(f"Gerente - Nome: {self.get_nome()} | Pagamento: R$ {self.calcular_pagamento():,.2f}")


class Empresa:
    """Gerencia os colaboradores da empresa."""

    def __init__(self, colaboradores: list):
        self._colaboradores = colaboradores

    def listar_pagamentos(self):
        for colaborador in self._colaboradores:
            colaborador.exibir_detalhes()

# Testes
if __name__ == "__main__":
    print("=== TESTES DA CLASSE COLABORADOR ===")
    colaborador_base = Colaborador("João Base")
    colaborador_base.exibir_detalhes()
    print("Nome atual:", colaborador_base.get_nome())
    colaborador_base.set_nome("João Alterado")
    print("Nome alterado:", colaborador_base.get_nome())
    print()

    print("=== TESTES DA CLASSE FUNCIONARIO ===")
    funcionario = Funcionario("Ana", 3000)
    funcionario.exibir_detalhes()
    funcionario.set_salario(3500)
    funcionario.exibir_detalhes()
    funcionario.set_salario(-1000)  # Deve mostrar erro
    print()

    print("=== TESTES DA CLASSE FREELANCER ===")
    freelancer = Freelancer("Carlos", 50)
    freelancer.set_horas_trabalhadas(20)
    freelancer.exibir_detalhes()
    freelancer.set_horas_trabalhadas(-5)  # Deve mostrar erro
    freelancer.set_valor_hora(60)
    freelancer.set_horas_trabalhadas(10)
    freelancer.exibir_detalhes()
    print()

    print("=== TESTES DA CLASSE COMISSAO ===")
    comissao = Comissao(0.1)
    print("Comissão atual:", comissao.get_comissao())
    print("Comissão sobre R$5000 em vendas:", comissao.calcular_comissao(5000))
    comissao.set_comissao(0.15)
    print("Nova comissão sobre R$4000 em vendas:", comissao.calcular_comissao(4000))
    comissao.calcular_comissao(-100)  # Deve mostrar erro
    print()

    print("=== TESTES DA CLASSE GERENTE ===")
    gerente = Gerente("Fernanda", 5000, 0.05)
    gerente.set_vendas(20000)
    gerente.exibir_detalhes()
    gerente.set_vendas(-3000)  # Deve mostrar erro
    print()

    print("=== TESTES DA CLASSE EMPRESA ===")
    empresa = Empresa([funcionario, freelancer, gerente])
    empresa.listar_pagamentos()
