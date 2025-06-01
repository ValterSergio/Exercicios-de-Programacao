from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QGridLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from dateutil.relativedelta import relativedelta
from datetime import datetime

# Variáveis globais
NOME = None
ANO = None
MES = None
DIA = None
RESULTADO = None  # QLabel para exibir o resultado

# Função para Verificar a idade
def Verificar_idade(ano: int, mes: int, dia: int) -> str:
    try:
        data_nascimento = datetime(ano, mes, dia)
    except ValueError:
        return f"Data de nascimento inválida!"

    data_atual = datetime.now()

    if data_nascimento > data_atual:
        return "Data de nascimento no futuro!"

    idade = relativedelta(data_atual, data_nascimento)

    if idade.years > 100:
        return "Não permitido: usuários com mais de 100 anos"

    if idade.years <= 18:
        return "Menores de idade não permitido"
    
    return f"Idade: {idade.years} anos, {idade.months} meses e {idade.days} dias"

# Um QLabel dizendo - seja bem vindo
def criar_saudacao(layout_base: QGridLayout):
    texto = QLabel("--- Seja Bem Vindo ---")
    texto.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout_base.addWidget(texto, 0, 0, 1, 2)

# Um QLabel com 'Nome: ' e um QlineEdit em branco para receber o nome do usuario
def obter_nome(layout_base: QGridLayout):
    global NOME

    nome = QLabel("Digite seu Nome: ")
    NOME = QLineEdit("")
    layout_base.addWidget(nome, 2, 0)
    layout_base.addWidget(NOME, 2, 1)

# Um Qlabel com 'Ano de Nascimento: ' e um QLineEdit para receber o valor
def obter_ano(layout_base: QGridLayout):
    global ANO
    
    ano = QLabel("Digite o Ano de Nascimento: ")
    ANO = QLineEdit("")
    
    layout_base.addWidget(ano, 3, 0)
    layout_base.addWidget(ANO, 3, 1)

# Um Qlabel com 'Mês de Nascimento: ' e um QLineEdit para receber o valor
def obter_mes(layout_base: QGridLayout):
    global MES

    mes = QLabel("Digite o Mês de Nascimento: ")
    MES = QLineEdit("")

    layout_base.addWidget(mes, 4, 0)
    layout_base.addWidget(MES, 4, 1)

# Um Qlabel com 'Dia de Nascimento: ' e um QLineEdit para receber o valor
def obter_dia(layout_base: QGridLayout):
    global DIA

    dia = QLabel("Digite o Dia de Nascimento: ")
    DIA = QLineEdit("")
    
    layout_base.addWidget(dia, 5, 0)
    layout_base.addWidget(DIA, 5, 1)

# Um QPushButton para Verificar a idade
def botao_Verificar(layout_base: QGridLayout):
    botao = QPushButton("Verificar Idade")
    
    # função para Verificar a idade
    botao.clicked.connect(lambda: exibir_resultado())
    layout_base.addWidget(botao, 6, 0, 1, 2)

# Um Qlabel Informando o resultado da validação
def exibir_resultado():
    global ANO, MES, DIA, RESULTADO
    try:
        ano = int(ANO.text())
        mes = int(MES.text())
        dia = int(DIA.text())
        mensagem = Verificar_idade(ano, mes, dia)
    except ValueError:
        mensagem = "Por favor, preencha todos os campos corretamente."

    RESULTADO.setText(mensagem)

def executar():
    # iniciando programa
    app = QApplication()

    # janela Base
    janela_base = QMainWindow()
    janela_base.setWindowTitle("Verificar Idade")

    widget_central = QWidget()
    layout_base = QGridLayout()

    # Um QLabel dizendo - seja bem vindo
    criar_saudacao(layout_base)

    # Um QLabel com 'Nome: ' e um QlineEdit em branco para receber o nome do usuario
    obter_nome(layout_base)

    # Um Qlabel com 'Ano de Nascimento: ' e um QLineEdit para receber o valor
    obter_ano(layout_base)

    # Um Qlabel com 'Mês de Nascimento: ' e um QLineEdit para receber o valor
    obter_mes(layout_base)

    # Um Qlabel com 'Dia de Nascimento: ' e um QLineEdit para receber o valor
    obter_dia(layout_base)

    # Um QPushButton para Verificar a idade
    botao_Verificar(layout_base)

    # Um Qlabel Informando o resultado da validação
    global RESULTADO
    RESULTADO = QLabel("")
    RESULTADO.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout_base.addWidget(RESULTADO, 7, 0, 1, 2)

    # finalizando programa
    widget_central.setLayout(layout_base) # definindo o layout base no widget central
    janela_base.setCentralWidget(widget_central) # definindo widget central
    janela_base.show()

    app.exec()

if __name__ == "__main__":
    executar()