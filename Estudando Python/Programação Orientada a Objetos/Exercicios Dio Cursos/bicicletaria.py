class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.parada = True
        self.velocidade_max = 50
        self.velocidade_atual = 0

    def buzinar(self):
        print("tlim tlim...")

    def freiar(self):
        print(f"Freio acionado")
        if self.velocidade_atual:
            self.parada = False
            self.velocidade_atual -= 1
            print(f"Reduzindo: {self.velocidade_atual} km/h")
        
        if self.velocidade_atual <= 0:
            self.parada = True

        if self.parada:
            print("Bicicleta está parada...")

    def acelerar(self):
        print("Acelerador acionado")
        self.velocidade_atual += 1
        print(f"Acelerando: {self.velocidade_atual} km/h")
    


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


if __name__ == "__main__":
    b1 = Bicicleta("Verde", "Monarc", "2015", 650)
    b1.acelerar()
    b1.acelerar()
    b1.freiar()
    b1.freiar()