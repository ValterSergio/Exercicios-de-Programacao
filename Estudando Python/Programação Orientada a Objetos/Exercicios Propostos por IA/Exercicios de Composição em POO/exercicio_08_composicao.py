from datetime import datetime


# Veiculo Base - Todo tipo de Nave é um Veiculo Espacial
class VeiculoEspacial:
    def __init__(self, nome: str, carga: list):
        self._nome = nome
        self.__carga = carga
    
    # metodos para nome
    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> bool:
        try:
            self._nome = nome
            print(f"Nave renomeada para: {self.get_nome()}")
            return True
        except Exception as erro:
            print(f"Erro - Atualizando o nome da {self.__class__.__name__}: {str(erro)}")
            return False

    # metodos para carga
    def get_carga(self) -> list:
        return self.__carga
    
    def _set_carga(self, nova_carga: list) -> bool:
        try:
            if isinstance(nova_carga, list):
                self.__carga = nova_carga
                print(f'Troca de Carga efetuada')
                return True
            print("Troca não efetuada, Carga não é uma lista")
            return False
        except Exception as erro:
            print(f"ERRO - Troca de carga da {self.__class__.__name__}: {str(erro)}")
            return False
    
    def exibir_carga(self) -> None:
        print("-"*65)
        print("\t\tGerenciamento de Carga")
        print("-"*65)
        if len(self.get_carga()) <= 0:
            print("Nave Vazia")

        for item in self.get_carga():
            print(item) 
        print("-"*65)
           
# Veiculos Espaciais podem ser separados
# - Nave de transporte ( transporte de passageiros )
class NaveTransporte(VeiculoEspacial):
    def __init__(self, nome, carga):
        super().__init__(nome, carga)


# - Nave de carga ( transporte de materiais )
class NaveCarga(VeiculoEspacial):
    def __init__(self, nome, carga):
        super().__init__(nome, carga)


# - Nave de Luxo ( transporte de V.I.P's )
class NaveLuxo(VeiculoEspacial):
    def __init__(self, nome, carga):
        super().__init__(nome, carga)


# Toda Nave Espacial precisa de um tripulante ( Nave tem Tripulante)

# Tripulantes podem ter varios perfils ( Piloto, Engenheiro, Médico)
class Tripulante:
    def __init__(self, nome: str, cargo: str):
        self.nome = nome
        self.cargo = cargo
    
    def get_nome(self):
        return self.nome
    
    def get_cargo(self):
        return self.cargo
    
    def exibir_informacoes(self):
        print(f"Nome: {self.get_nome()} | Cargo: {self.get_cargo()}")

class Piloto(Tripulante):
    def __init__(self, nome):
        super().__init__(nome, cargo="Piloto")

class Engenheiro(Tripulante):
    def __init__(self, nome):
        super().__init__(nome, cargo="Engenheiro")

class Medico(Tripulante):
    def __init__(self, nome):
        super().__init__(nome, cargo="Médico")

class Evento:
    def __init__(self, evento: str):
        self.horario = datetime.now().strftime("Dia: %d/%m/%Y\tHora: %H:%M:%S")
        self.evento = evento
    
    def get_horario(self):
        return self.horario
    
    def get_evento(self):
        return self.evento
    
    def exibir_evento(self):
        print(f"horario do evento: {self.get_horario()}")
        print(f"Evento Ocorrido: {self.get_evento()}")

class Comunicacao:
    def __init__(self, remetente: object, destinatario: object):
        self.remetente = remetente
        self.destinatario = destinatario
        
    
    def enviar_mensagem(self, mensagem: str):
        return {
        "Remetente": self.remetente.get_nome(),
        "Destinatario": self.destinatario.get_nome(),
        "Data da Mensagem": datetime.now().strftime("%d/%m/%Y"),
        "Hora da Mensagem": datetime.now().strftime("%H:%M:%S"),
        "Mensagem": mensagem
    }
    
class Carga:
    def __init__(self, nome: str, peso: float, categoria: str):
        self.nome = nome
        self.peso = peso
        self.categoria = categoria
    
    def __str__(self):
        return f"Nome: {self.nome} | Peso: {self.peso} Kg | Categoria: {self.categoria}"
    
class Missao:
    def __init__(self, nome_da_missao: str, nave_designada: object, origem: str, destino: str, tripulantes: list[object]):
        self.registro_de_eventos = [
            Evento("Ligando Sistema Eletrico"),
            Evento("Ligando Motores"),
            Evento("Recebendo Missao"),
            Evento("Verificando Destino da Missão"),
            Evento("Preparando Decolagem"),
            Evento("Iniciar Decolagem")
        ]
        self.nome_missao = nome_da_missao
        self.nave_da_missao = nave_designada
        self.origem = origem
        self.destino = destino
        self.tripulantes = tripulantes
        self.lista_mensagens = []

    def exibir_tripulacao(self):
        for tripulante in self.tripulantes:
            tripulante.exibir_informacoes()
    
    def adicionar_tripulante(self, tripulante: object):
        self.tripulantes.append(tripulante)
    
    def remover_tripulantes(self, nome: str):
        self.tripulantes = [x for x in self.tripulantes if x.get_nome().lower() != nome.lower()]
    
    def exibir_eventos(self):
        for evento in self.registro_de_eventos:
            evento.exibir_evento()
    
    def registrar_evento(self, evento: str):
        self.registro_de_eventos.append(Evento(evento))
    
    def receber_mensagem(self, mensagem: dict ):
        mensagem["Status de Leitura"] = False
        self.lista_mensagens.append(mensagem)
    
    def exibir_mensagens_nao_lidas(self):
        for msg in self.lista_mensagens:
            if not msg["Status de Leitura"]:
                for x, y in msg.items():
                    print(x, y)

    def informacoes_da_missao(self):
        print("Nome da Missão: ", self.nome_missao)
        print("Nave utilizada: ", self.nave.get_nome())
        print("\t\t Tripulantes a Bordo")
        self.exibir_tripulacao()
        print("\t\tRegistro de Cargas")
        self.nave_da_missao.exibir_carga()
        print("\t\tRegistros de Viagem")
        self.exibir_eventos()
    
if __name__ == "__main__":
    # Criando carga
    carga1 = Carga("Oxigênio", 1200.5, "Essencial")
    carga2 = Carga("Comida", 800.0, "Suprimentos")
    
    # Criando nave
    nave = NaveCarga("Explorer I", [carga1, carga2])
    
    # Exibindo carga da nave
    nave.exibir_carga()
    
    # Criando tripulantes
    piloto = Piloto("John Shepard")
    engenheiro = Engenheiro("Tali'Zorah")
    medico = Medico("Mordin Solus")
    
    # Criando missão
    missao = Missao("Missão Alfa", nave, "Terra", "Marte", [piloto, engenheiro])
    
    # Adicionando médico
    missao.adicionar_tripulante(medico)
    
    # Exibindo tripulação
    print("\nTripulação da missão:")
    missao.exibir_tripulacao()
    
    # Exibindo eventos
    print("\nEventos registrados:")
    missao.exibir_eventos()
    
    # Comunicação entre tripulantes
    comunicacao = Comunicacao(piloto, engenheiro)
    mensagem = comunicacao.enviar_mensagem("Checar o motor principal.")
    missao.receber_mensagem(mensagem)
    
    print("\nMensagens não lidas:")
    missao.exibir_mensagens_nao_lidas()
