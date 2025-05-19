from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy
from sys import argv

app = QApplication(argv)

janela = QWidget()

# define um titulo para a janela do widget
janela.setWindowTitle("Primeiro Widget")

# define uma imagem de fundo basica para janela
janela.setStyleSheet("background-image: url('modelo_basico.png');")

# exibe o widget 
janela.show()
largura = janela.width()
altura = janela.height()

print(largura, altura)
# inicia o loop de eventos
app.exec()