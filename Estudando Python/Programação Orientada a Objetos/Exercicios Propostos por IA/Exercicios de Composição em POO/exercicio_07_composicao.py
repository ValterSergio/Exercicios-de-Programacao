"""
Desafio: Sistema de Monitoramento de Viagem Espacial (Refatorado)

Este sistema simula o monitoramento de uma missão espacial,
controlando as naves, os astronautas a bordo e os eventos
registrados durante a missão.
"""

from datetime import datetime


def separador():
    print("-" * 65)


class Evento:
    def __init__(self, descricao: str):
        self.horario = datetime.now().strftime("Data: %d/%m/%Y - Hora: %H:%M:%S")
        self.descricao = descricao

    def exibir_descricao(self):
        separador()
        print(f"Hora do Evento: {self.horario}")
        print(f"Descrição do Evento: {self.descricao}")


class Missao:
    def __init__(self, nome: str, astronautas: list):
        self.nome_missao = nome
        self.lista_astronautas = astronautas
        self.registro_de_eventos = [
            Evento("Verificação de Sistemas Concluída"),
            Evento(f"Missão {nome} iniciada")
        ]

    def registrar_evento(self, descricao: str):
        self.registro_de_eventos.append(Evento(descricao))

    def exibir_tripulacao(self):
        separador()
        print("\t\tTripulação a Bordo")
        separador()
        for a in self.lista_astronautas:
            a.exibir_astronauta()
        separador()

    def exibir_eventos(self):
        separador()
        print("\t\tRegistro de Eventos")
        for evento in self.registro_de_eventos:
            evento.exibir_descricao()
        separador()


class NaveEspacial:
    def __init__(self, nome: str, missao: Missao):
        self.nome_nave = nome
        self.missao = missao

    def status_geral(self):
        separador()
        print(f"\t\tNave {self.nome_nave}")
        print(f"\t\tMissão: {self.missao.nome_missao}")
        separador()
        print("\t\tRegistro de Bordo")
        separador()
        self.missao.exibir_tripulacao()
        self.missao.exibir_eventos()


class Astronauta:
    def __init__(self, nome: str, nacionalidade: str, cargo: str):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.cargo = cargo

    def exibir_astronauta(self):
        print(f"Nome: {self.nome} | Nacionalidade: {self.nacionalidade} | Cargo: {self.cargo}")


if __name__ == "__main__":
    a1 = Astronauta("Valter", "Brasil", "Piloto")
    a2 = Astronauta("Wagner", "Brasil", "Co-piloto")
    a3 = Astronauta("Wando", "Brasil", "Cientista")
    a4 = Astronauta("Wictor", "Brasil", "Coronel")
    a5 = Astronauta("Wanderley", "Brasil", "Comandante de Armas")

    astronautas = [a1, a2, a3, a4, a5]
    missao1 = Missao("Missao1", astronautas)

    missao1.exibir_eventos()

    missao1.registrar_evento("Ligando Motores !!")
    missao1.registrar_evento("Iniciando Decolagem !!!")
    missao1.exibir_eventos()

    nave = NaveEspacial("X1", missao1)
    nave.status_geral()
