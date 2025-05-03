class Anotacao:
    def __init__(self, horario: str, texto: str):
        """
        Inicializa uma anotação com horário e texto.

        Args:
            horario (str): Horário da anotação (formato livre).
            texto (str): Conteúdo da anotação.
        """
        self.horario = horario
        self.texto = texto

    def __str__(self):
        """Retorna a anotação em formato de string legível."""
        return f"Hora: {self.horario} | Anotação: {self.texto}"


class Reuniao:
    def __init__(self, titulo: str, data: str, anotacao_class):
        """
        Inicializa uma reunião com título, data e anotações pré-definidas.

        Args:
            titulo (str): Título da reunião.
            data (str): Data da reunião (formato livre).
            anotacao_class (type): Classe usada para criar as anotações.
        """
        self.titulo = titulo
        self.data = data

        # Instancia duas anotações iniciais usando a classe passada
        self.lista_de_anotacao = [
            anotacao_class("23:56", "Começando reunião."),
            anotacao_class("23:59", "Faltaram 3 pessoas")
        ]

    def exibir_relatorio(self):
        """Exibe um relatório da reunião com todas as anotações."""
        print("-" * 65)
        print("Reunião dos Sócios")
        print("-" * 65)
        print("Título:", self.titulo, "| Data:", self.data)
        print("-" * 65)
        for anotacao in self.lista_de_anotacao:
            print(anotacao)


# Teste do funcionamento da classe Reuniao
if __name__ == "__main__":
    # Criando uma reunião com anotações iniciais
    a = Reuniao("Reunião de Planejamento", "21/04/2025", Anotacao)
    a.exibir_relatorio()
