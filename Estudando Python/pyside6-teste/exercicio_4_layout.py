from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from sys import argv

def cabecalho(msg: str) -> None:
    print("-"*65)
    print("--- ", msg)
    print("-"*65)

app = QApplication(argv)

janela = QWidget()

# define um titulo para a janela do widget
janela.setWindowTitle("Primeiro Widget")

# define uma imagem de fundo basica para janela
janela.setStyleSheet("background-image: url('modelo_basico.png');")


# obtem largura e altura do widget inicial
largura_inicial = janela.width()
altura_inicial = janela.height()

# vamos definir o limite das janelas 
janela.setMaximumWidth(largura_inicial)
janela.setMaximumHeight(altura_inicial + 100)

# tamanho inicial da janela
janela.resize(int(largura_inicial), int(altura_inicial+100))

# obtem largura e altura do widget para confirmar alterações
largura_modificada = janela.width()
altura_modificada = janela.height()

""" Criando um layout para adicionar dentro do widget"""
layout_vertical = QVBoxLayout()

# precisamos de algo para esse layout 3 botoes basicos
botao1 = QPushButton("1° botão")
botao2 = QPushButton("2° botão")
botao3 = QPushButton("3° botão")

# e um texto para dar vida ao botões
# Cria o texto (QLabel) e adiciona ao layout
texto = QLabel("Escolha uma das opções abaixo:")

# vamos modificar a cor dos textos para eles ficarem visiveis
botao1.setStyleSheet("font-size: 30px; color: black; background: transparent")
botao2.setStyleSheet("font-size: 30px; color: black; background: transparent")
botao3.setStyleSheet("font-size: 30px; color: black; background: transparent")

# vamos modificar o texto também
texto.setStyleSheet("font-size: 30px; color: black;")

# adicionamos o texto ao layout 
layout_vertical.addWidget(texto, alignment=Qt.AlignTop | Qt.AlignLeft)

# podemos adicionar os botoes ao layout e alinhar eles a esquerda
layout_vertical.addWidget(botao1, alignment=Qt.AlignLeft)
layout_vertical.addWidget(botao2, alignment=Qt.AlignLeft)
layout_vertical.addWidget(botao3, alignment=Qt.AlignLeft)

# vamos gerar ações basicas nos botões
def conectar_botao(msg: str):
    print("Eu sou o botao ", msg)

botao1.clicked.connect(lambda : conectar_botao("1"))
botao2.clicked.connect(lambda : conectar_botao("2"))
botao3.clicked.connect(lambda : conectar_botao("3"))

# adicionar margens e espaçamento
layout_vertical.setContentsMargins(20, 20, 20, 20)  # margens esquerda, topo, direita, baixo
layout_vertical.setSpacing(5)  # espaço entre widgets


# agora temos que adicionar o layout a janela superior( widget)
janela.setLayout(layout_vertical)

# exibe as modificações realizadas no tamanho
print(f"Largura inicial: {largura_inicial}\nAltura Inicial: {altura_inicial}")
print(f"Largura modificada: {largura_modificada}\nAltura modificada: {altura_modificada}")

# exibe o widget 
janela.show()
# inicia o loop de eventos
app.exec()
