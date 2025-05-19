""" queroo criar um widget que tenha 3 botões
um botão para executar ou pausar, um para a proxima musica e a outra para a musica anterior
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

def gerar_rotulo(texto: str) -> QLabel:
    rotulo = QLabel(texto.capitalize())
    rotulo.setStyleSheet("background-color: white; color: black; font-size: 30px;")
    rotulo.setAlignment(Qt.AlignCenter)
    return rotulo

def gerar_botao(texto: str) -> QPushButton:
    botao = QPushButton(texto.capitalize())
    botao.setStyleSheet("background-color: white; color: black; font-size: 15px;")
    botao.clicked.connect(lambda: print(f"Clicaram em Mim: {texto.capitalize()}"))
    return botao

def gerar_layout() -> QVBoxLayout:
    layout = QVBoxLayout()
    layout.setSpacing(1)
    return layout

def coluna_central():
    texto_saudacao = gerar_rotulo("Adicionar layout")
    botao1 = gerar_botao("Proximo")
    botao2 = gerar_botao("Anterior")
    botao3 = gerar_botao("reproduzir/pausar")
    layout = gerar_layout()
    widget = QWidget()
    layout.addWidget(texto_saudacao)
    layout.addWidget(botao1)
    layout.addWidget(botao2)
    layout.addWidget(botao3)
    widget.setLayout(layout)
    return widget