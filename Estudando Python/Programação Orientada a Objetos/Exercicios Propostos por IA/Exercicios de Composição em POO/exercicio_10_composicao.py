from datetime import datetime
from time import sleep 

def linha_delimitadora():
    return f"{'-'*65}\n"

class Hospede:
    def __init__(self, nome: str, email: str, telefone: str):
        self._nome = nome
        self._email = email
        self._telefone = telefone
    
    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email
    
    def get_telefone(self):
        return self._telefone

    def set_nome(self, novo_nome: str):
        self._nome = novo_nome
    
    def set_email(self, novo_email: str):
        self._email = novo_email
    
    def set_telefone(self, novo_telefone: str):
        self._telefone = novo_telefone

    def exibir_hospede(self):
        return f"{linha_delimitadora()}\t\tDados pessoais do Hospede\n{linha_delimitadora()}Nome: {self.get_nome()}\nEmail: {self.get_email()}\nTelefone: {self.get_telefone()}\n{linha_delimitadora()}"
    
class Quarto:
    def __init__(self, numero_do_quarto: str):
        self.numero_do_quarto = numero_do_quarto
        self.ocupado = False
        self.valor_do_quarto = 5
    
    def get_valor_do_quarto(self):
        return self.valor_do_quarto
    
    def set_valor_do_quarto(self, valor: int):
        if valor > 0:
            self.valor_do_quarto = valor

    def get_status_ocupado(self):
        return "Ocupado" if self.ocupado else "Livre"
    
    def ocupar_quarto(self):
        self.ocupado = True

    def liberar_quarto(self):
        if  self.ocupado:
            self.ocupado = False
        
    def exibir_quarto(self):
        print(linha_delimitadora(), end="")
        print("Numero do Quarto: ", self.numero_do_quarto)
        print("Estado do Quarto: ", self.get_status_ocupado())
        print(linha_delimitadora(), end="")

class Servicos:
    def __init__(self):
        self.servicos =  [
            {"Trocar Toalhas": "Não realizada"},
            {"Trocar Lencois": "Não realizada"},
            {"Limpar o chão": "Não realizada"},
            {"Remover pó dos moveis": "Não realizada"},
            {"Lavar Banheiro": "Não realizada"},
            {"Descontaminar Quarto": "Não realizada"}
        ]

    def atualizar_lista(self, lista: list[dict]):
        self.servicos = lista

    def realizar_tarefas(self):
        for servico in self.servicos:
            for tarefa, _ in servico.items():
                servico[tarefa] = "Realizada"

    def exibir_servicos(self):
        print(linha_delimitadora(), end="")
        print("Exibindo Serviços")
        print(linha_delimitadora(), end="")
        for servico in self.servicos:
            for tarefa, estado in servico.items():
                print(f"{tarefa}: {estado}")
        print(linha_delimitadora(), end="")

    def adicionar_tarefa(self, tarefa: str):
        guardar = {str(tarefa.capitalize()): "Não realizada"}
        self.servicos.append(guardar)
    
    def remover_tarefa(self, tarefa: str):
        # função cocm logica não pythonica
        lista = []
        for servico in self.servicos:
            try:
                if servico[tarefa]:
                    print("Chave Encontrada")
            except KeyError:
                print("Chave não existe")
                lista.append(servico)
        self.servicos = lista
    
class QuartoSimples(Quarto):
    def __init__(self, numero_do_quarto: int,):
        super().__init__(numero_do_quarto)
        self.set_valor_do_quarto(10)
        self.entrada = datetime.now().strftime(f"{linha_delimitadora()}Data: %d/%m/%YHora: %H:%M")
        
        # definindo servicos do quarto simples
        self.servicos = Servicos()
        self.servicos.adicionar_tarefa("Telefone com recepção")
        self.servicos.adicionar_tarefa("Wifi")
    
    def exibir_quarto(self):
        print(linha_delimitadora(), end="")
        print("\t\tInformações do Quarto")
        print(linha_delimitadora(), end="")
        print("Numero do Quarto: ", self.numero_do_quarto)
        print("Estado do Quarto: ", self.get_status_ocupado())
        print(linha_delimitadora(), end="")

    def exibir_servicos(self):
        self.servicos.exibir_servicos()
    
    def cancelar_reserva(self):
        print("Cancelando reserva")
        
class QuartoLuxo(Quarto):
    def __init__(self, numero_do_quarto: int,):
        super().__init__(numero_do_quarto)
        self.set_valor_do_quarto(30)
        self.entrada = datetime.now().strftime(f"{linha_delimitadora()}Data: %d/%m/%YHora: %H:%M")
        
        # definindo servicos do quarto simples
        self.servicos = Servicos()
        self.servicos.adicionar_tarefa("Telefone com recepção")
        self.servicos.adicionar_tarefa("Wifi")
        self.servicos.adicionar_tarefa("Café da Manhã")
        self.servicos.adicionar_tarefa("Ar-condicionado")
        self.servicos.adicionar_tarefa("Tv a Cabo")
        self.servicos.adicionar_tarefa("5 Preservativos")
        
    def exibir_quarto(self):
        print(linha_delimitadora(), end="")
        print("\t\tInformações do Quarto")
        print(linha_delimitadora(), end="")
        print("Numero do Quarto: ", self.numero_do_quarto)
        print("Estado do Quarto: ", self.get_status_ocupado())
        print(linha_delimitadora(), end="")
    
    def exibir_servicos(self):
        self.servicos.exibir_servicos()

class Reserva():
    def __init__(self, cliente: Hospede, quarto: object, horas):
        self.cliente = cliente
        self.quarto = quarto
        self.horas = horas
        self.receber_cliente()
    
    def acompanhar_reserva(self):
        converter_para_minutos = self.horas * 60
        converter_minutos_para_segundos = converter_para_minutos * 60

        tempo_por_tarefa = converter_minutos_para_segundos / len(self.quarto.servicos.servicos)
        for servico in self.quarto.servicos.servicos:
            for tarefa, _ in servico.items():
                print("Sujando o quarto")
                servico[tarefa] = "Não Realizado"
                # sleep(tempo_por_tarefa)
        print("Fim de Hospedagem - por favor liberar o quarto")
        return True      

    def receber_cliente(self):
        # mudar quarto para ocupado
        self.quarto.ocupar_quarto()
    
    def calcular_reserva(self):
        return self.horas * self.quarto.get_valor_do_quarto()
    
    def liberar_reserva(self):
        self.quarto.liberar_quarto()
    
    def exibir_reserva(self):
        print(linha_delimitadora(), end="")
        print("Cliente Hospedado: ", self.cliente.get_nome())
        print("Quarto Ocupado: ", self.quarto.numero_do_quarto)
        tipo_de_servico = "Convencional" if self.quarto.__class__.__name__ == "QuartoSimples" else "Quarto V.I.P"
        print("Atendimento: ", tipo_de_servico)
        print("Horas Reservadas: ", self.horas, " Hrs")
        print(f"Valor Final:  R$ {self.calcular_reserva():,.2f}")
        print(linha_delimitadora(), end="")

if __name__ == "__main__":

    # teste de Hospede
    def testar_metodos_hospede():
        h1 = Hospede("valter", "valter@email.com", "99 9999 99999")
        print(h1.exibir_hospede())
        h1.set_email("vater@gmail.com")
        h1.set_nome("Walter")
        h1.set_telefone("11 1111 11111")
        print(h1.exibir_hospede())

    def testar_metodos_quarto():
        # testar Quarto padrão
        q1 = Quarto(32)

        print(linha_delimitadora(), end="")
        print("\t\tTestar tarefas")
        print(linha_delimitadora(), end="")
        print(" --- Quarto padrão")
        # verificar detalhes do quarto
        q1.exibir_quarto()

        # realizar serviços
        print("Testar Realização de Serviços")
        print(linha_delimitadora(), end="")
        q1.realizar_tarefas()
        print("--- Quarto apos realizar serviços")
        q1.exibir_quarto()

        print("\t\tTestar adicionar cliente")
        print(linha_delimitadora(), end="")
        q1.ocupar_quarto()
        print("--- Atualizando status do cliente")
        q1.exibir_quarto()

        print("Testar Liberar cliente")
        print(linha_delimitadora(), end="")
        print("--- liberando cliente")
        q1.liberar_quarto()
        q1.exibir_quarto()
    
    # teste de Serviços
    def testar_metodos_servico():
        s1 = Servicos()
        s1.exibir_servicos()
        s1.realizar_tarefas()
        s1.exibir_servicos()
        s1.adicionar_tarefa("Lavar louça") # lavar louça dentro de um quarto ?
        s1.exibir_servicos()
        s1.remover_tarefa("Lavar louça")
        s1.exibir_servicos()

    def testar_metodos_quarto_simples():    
        qs1 = QuartoSimples(15)
        qs1.exibir_quarto()

    def testar_metodos_quarto_luxo():    
        qs1 = QuartoLuxo(10)
        qs1.exibir_quarto()


    def testar_metodo_reserva():
        # criando cliente
        cliente = Hospede("Valter", "asdaksdkas", "telefoneaskdna")

        # Criando o Quarto
        quarto1 = QuartoSimples(1)

        # criando a reserva
        r1 = Reserva(cliente, quarto1, 12)

        # Exibindo servicos do quarto
        r1.quarto.servicos.exibir_servicos()

        # Realizando limpeza do quarto
        quarto1.servicos.realizar_tarefas()
        
        # exibindo serviços realizados
        r1.quarto.servicos.exibir_servicos()

        # Exibindo detalhes do quarto
        quarto1.exibir_quarto()

        # acompanhando tempo de reserva
        if r1.acompanhar_reserva():
            r1.liberar_reserva()
        
        # Quarto está livre
        print()
        print(quarto1.get_status_ocupado())

        # informar o valor a pagar
        r1.exibir_reserva()
        print(r1.calcular_reserva())

    # testar_metodos_hospede()
    # testar_metodos_servico()
    # testar_metodos_quarto()
    # testar_metodos_quarto_simples()
    # testar_metodos_quarto_luxo()
    # testar_metodo_reserva()
