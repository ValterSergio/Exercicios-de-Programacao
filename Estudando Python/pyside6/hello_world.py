from PySide6.QtWidgets import QApplication, QPushButton
from random import choice

def alterar_tamanho(botao: QPushButton):
    tamanhos = [100, 200, 300, 400, 500]
    botao.setFixedSize(choice(tamanhos), choice(tamanhos))

def alterar_texto(botao: QPushButton):
    saudacoes = [
        "Seja bem-vindo",    # Português
        "Bienvenido",        # Espanhol
        "Welcome",           # Inglês
        "Bienvenue",         # Francês
        "Benvenuto"          # Italiano
]
    botao.setText(choice(saudacoes))

def mudar_cor(botao: QPushButton):
    """
    Função para mudar a cor do botão
    - As cores de fundo e de texto variam aleatoriamente entre 4 cores básicas
    - verde, vermelho, azul, amarelo

    Args:
        Um botão do tipo QPushButton
    
    """
    cores = ["green", 'red', 'blue', 'yellow']
    botao.setStyleSheet(f"background-color:{choice(cores)}; color: {choice(cores)}")

# inicia a aplicação
app = QApplication()

# cria um botão
botao_hello_world = QPushButton("Hello World")

# define um tamanho fixo para o botão
botao_hello_world.setFixedSize(200, 300)

# Conectar a função para mudar o botão de cor, texto original do botao, tamanho do botão
botao_hello_world.clicked.connect(lambda: mudar_cor(botao_hello_world))
botao_hello_world.clicked.connect(lambda: alterar_texto(botao_hello_world))
botao_hello_world.clicked.connect(lambda: alterar_tamanho(botao_hello_world))

# exibe o botão, que no momento está sendo a janela principal
botao_hello_world.show()

# executar o loop de eventos
app.exec()
