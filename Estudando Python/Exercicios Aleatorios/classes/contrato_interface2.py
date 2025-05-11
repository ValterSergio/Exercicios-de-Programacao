from abc import ABC, abstractmethod

class InterfaceVeiculo(ABC):
    def __init__(self, velocidade_maxima, aceleracao):
        self.velocidade_maxima = velocidade_maxima
        self._aceleracao = aceleracao

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def freiar(self):
        pass

class Fusca(InterfaceVeiculo):
    def __init__(self, velocidade_maxima, aceleracao):
        super().__init__(velocidade_maxima, aceleracao)
        self.velocidade_atual = 0

    @property
    def aceleracao(self):
        return self._aceleracao

    @aceleracao.setter
    def aceleracao(self, valor):
        if valor < 0:
            raise ValueError("A aceleração não pode ser negativa.")
        self._aceleracao = valor

    def acelerar(self):
        if self.velocidade_atual < self.velocidade_maxima:
            self.velocidade_atual += 1
        print(f"Acelerando: {self.velocidade_atual:,.2f} Km/h")

    def freiar(self):
        if self.velocidade_atual > 0:
            self.velocidade_atual -= 1
        print(f"Freando: {self.velocidade_atual:,.2f} Km/h")

# Teste
fusca = Fusca(10, 2)

while fusca.velocidade_atual < fusca.velocidade_maxima:
    fusca.acelerar()

while fusca.velocidade_atual > 0:
    fusca.freiar()
