from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QGridLayout, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

# função para lidar com o clique dos botões, recebendo o texto do botão
def clicar_botao(texto):
    if texto == "C":
        layout_visor.clear()
    elif texto == "=":
        try:
            resultado = str(eval(layout_visor.text()))
            layout_visor.setText(resultado)
        except Exception:
            layout_visor.setText("Erro")
    else:
        layout_visor.insert(texto)

def layout_teclado() -> QGridLayout:
    # criar um layout com numeros em baixo
    layout_numeros = QGridLayout()

    # criar os botões
    # -- botoes funcionais
    botao_resetar = QPushButton("C")
    botao_calcular = QPushButton("=")

    # -- botoes operadores
    botao_somar = QPushButton("+")
    botao_subtrair = QPushButton("-")
    botao_multiplicar = QPushButton("*")
    botao_dividir = QPushButton("/")

    # -- botoes numeros do teclado
    botao_zero = QPushButton("0")
    botao_um = QPushButton("1")
    botao_dois = QPushButton("2")
    botao_tres = QPushButton("3")
    botao_quatro = QPushButton("4")
    botao_cinco = QPushButton("5")
    botao_seis = QPushButton("6")
    botao_sete = QPushButton("7")
    botao_oito = QPushButton("8")
    botao_nove = QPushButton("9")

    # conectar os botões ao visor com lambda para passar texto
    botao_resetar.clicked.connect(lambda: clicar_botao("C"))
    botao_calcular.clicked.connect(lambda: clicar_botao("="))
    botao_somar.clicked.connect(lambda: clicar_botao("+"))
    botao_subtrair.clicked.connect(lambda: clicar_botao("-"))
    botao_multiplicar.clicked.connect(lambda: clicar_botao("*"))
    botao_dividir.clicked.connect(lambda: clicar_botao("/"))
    botao_zero.clicked.connect(lambda: clicar_botao("0"))
    botao_um.clicked.connect(lambda: clicar_botao("1"))
    botao_dois.clicked.connect(lambda: clicar_botao("2"))
    botao_tres.clicked.connect(lambda: clicar_botao("3"))
    botao_quatro.clicked.connect(lambda: clicar_botao("4"))
    botao_cinco.clicked.connect(lambda: clicar_botao("5"))
    botao_seis.clicked.connect(lambda: clicar_botao("6"))
    botao_sete.clicked.connect(lambda: clicar_botao("7"))
    botao_oito.clicked.connect(lambda: clicar_botao("8"))
    botao_nove.clicked.connect(lambda: clicar_botao("9"))

    # adicionar os botões ao layout
    # -- primeira linha
    layout_numeros.addWidget(botao_resetar, 0, 0)
    layout_numeros.addWidget(botao_um, 0, 1)
    layout_numeros.addWidget(botao_dois, 0, 2)
    layout_numeros.addWidget(botao_tres, 0, 3)

    # -- segunda linha
    layout_numeros.addWidget(botao_somar, 1, 0)
    layout_numeros.addWidget(botao_quatro, 1, 1)
    layout_numeros.addWidget(botao_cinco, 1, 2)
    layout_numeros.addWidget(botao_seis, 1, 3)

    # -- terceira linha
    layout_numeros.addWidget(botao_subtrair, 2, 0)
    layout_numeros.addWidget(botao_sete, 2, 1)
    layout_numeros.addWidget(botao_oito, 2, 2)
    layout_numeros.addWidget(botao_nove, 2, 3)

    # -- quarta linha
    layout_numeros.addWidget(botao_multiplicar, 3, 0)
    layout_numeros.addWidget(botao_dividir, 3, 1)
    layout_numeros.addWidget(botao_zero, 3, 2)
    layout_numeros.addWidget(botao_calcular, 3, 3)

    return layout_numeros

app = QApplication()

# criar uma janela primaria
janela_mae = QMainWindow()

# criar um widget central ( base para todos os outros widgets )
widget_central = QWidget()
widget_central.setStyleSheet("background-color: black; color: white;")

# criar um visor para receber as operações do usuario
layout_visor = QLineEdit()
layout_visor.setPlaceholderText("Calculadora do tio...")
layout_visor.setReadOnly(True)
layout_visor.setAlignment(Qt.AlignRight)
layout_visor.setStyleSheet("font-size: 24px; padding: 5px;")

# criar o layout com os botões
layout_numeros = layout_teclado()

'''
Um layout vertical para receber o layout do visor e o layout do teclado
'''
layout_principal = QVBoxLayout()
layout_principal.addWidget(layout_visor)
layout_principal.addLayout(layout_numeros)

# adicionar o layout no widget
widget_central.setLayout(layout_principal)
widget_central.adjustSize()
janela_mae.setCentralWidget(widget_central)
janela_mae.show()
app.exec()
