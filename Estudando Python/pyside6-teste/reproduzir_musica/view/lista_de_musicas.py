from PySide6.QtWidgets import QListWidget, QListWidgetItem, QApplication, QWidget
from PySide6.QtCore import Qt
from reproduzir_musica.model.auxiliares import obter_duracao, converter_segundos
from reproduzir_musica.model.encontrar_musicas import filtrar_arquivos_mp3
from reproduzir_musica.model.dados import RegistrarMusicas

def lista_de_musicas2():
    musicas_localizadas = RegistrarMusicas()

    lista_view = QListWidget()
    for musica in musicas_localizadas.lista_de_musicas:
        opcao = QListWidgetItem()
        nome = musica.get_nome_musica()
        duracao = musica.get_duracao()
        opcao.setText(f"Nome: {nome.capitalize()} | Duração: {duracao}")
        lista_view.addItem(opcao)
    lista_view.setStyleSheet("background-color: white; color: black; font-size: 15px;")
    lista_view.setItemAlignment(Qt.AlignCenter)
    return lista_view

# def lista_de_musicas(lista_de_caminhos: list[dict]):
#     lista = QListWidget()
#     musicas_encontradas = lista_de_caminhos
#     cont = 0
#     for musica in musicas_encontradas:
#         opcao = QListWidgetItem()
#         opcao.setText(f"Nome: {musica['Nome']} \n --- Duração: {converter_segundos(obter_duracao(musica['caminho']))} \n --- Posição: {cont}")
#         lista.addItem(opcao)
#         cont += 1
#     lista.setStyleSheet("background-color: white; color: black; font-size: 15px;")
#     lista.setItemAlignment(Qt.AlignCenter)
#     return lista

if __name__ == "__main__":
    app = QApplication([])
    janela_teste = QWidget()
    # coluna_musica = lista_de_musicas()
    janela_teste.setLayout(lista_de_musicas2())
    janela_teste.show()
    app.exec()