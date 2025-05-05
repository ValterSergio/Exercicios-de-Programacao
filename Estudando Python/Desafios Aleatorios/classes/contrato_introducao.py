from abc import ABC, abstractmethod

class MeioDeTransporte(ABC):  # Classe abstrata = contrato
    @abstractmethod
    def mover(self):
        pass  # qualquer classe concreta deve implementar isso

    @abstractmethod
    def combustivel(self):
        pass

class Carro(MeioDeTransporte):
    @property
    def mover(self):
        return "Dirigindo..."

    @property
    def combustivel(self):
        return "Combustão Gasolina"

class Bicicleta(MeioDeTransporte):
    @property
    def mover(self):
        return "Pedalando..."

    @property
    def combustivel(self):
        return "Energia Humana"


lista = []
for x in range(20):
    carro = Carro()
    bike = Bicicleta()
    lista.append(carro)
    lista.append(bike)

for x in lista:
    print("-"*65)
    print("--- Dados de Veiculo")
    print("-"*65)
    print(f"Classe Atual: {x.__class__.__name__}")
    print(f"Tipo de movimento: {x.mover}")
    print(f"Tipo de combustivel: {x.combustivel}\n")