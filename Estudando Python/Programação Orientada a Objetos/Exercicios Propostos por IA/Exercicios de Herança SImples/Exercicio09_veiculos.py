class Veiculo:
    def __init__(self, placa, marca, modelo, ano):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def _dados_basicos(self):
        return f"{self._marca} {self._modelo} - {self._ano} | Placa: {self._placa}"

class Carro(Veiculo):
    def __init__(self, placa, marca, modelo, ano, portas):
        super().__init__(placa, marca, modelo, ano)
        self._portas = portas

    def mostrar_dados(self):
        print(f"{self._dados_basicos()} | Portas: {self._portas}")

class Moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, cilindradas):
        super().__init__(placa, marca, modelo, ano)
        self._cilindradas = cilindradas

    def mostrar_dados(self):
        print(f"{self._dados_basicos()} | Cilindradas: {self._cilindradas}")

if __name__ == "__main__":
    # Teste da classe Carro
    print("Teste da classe Carro")
    carro = Carro("ABC1234", "Toyota", "Corolla", 2022, 4)
    carro.mostrar_dados()
    print()

    # Teste da classe Moto
    print("Teste da classe Moto")
    moto = Moto("XYZ5678", "Honda", "CB500", 2021, 500)
    moto.mostrar_dados()
    print()
