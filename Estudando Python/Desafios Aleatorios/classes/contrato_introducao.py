from abc import ABC, abstractmethod

class MeioDeTransporte(ABC):  # Classe abstrata = contrato
    @abstractmethod
    def mover(self):
        pass  # qualquer classe concreta deve implementar isso

class Carro(MeioDeTransporte):
    def mover(self):
        print("Dirigindo...")

class Bicicleta(MeioDeTransporte):
    def mover(self):
        print("Pedalando...")
