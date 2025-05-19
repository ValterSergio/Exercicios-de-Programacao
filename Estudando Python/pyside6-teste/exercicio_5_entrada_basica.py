from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QSizePolicy
)
from PySide6.QtCore import Qt

# 1. Criar o app
app = QApplication([])

# 2. Criar a janela principal
janela = QWidget()
janela.setWindowTitle("Formulário Profissional")
janela.resize(800, 800)
janela.setStyleSheet("background-color: lime;")

# 3. Criar layout principal
layout = QVBoxLayout()
layout.setContentsMargins(60, 60, 60, 60)
layout.setSpacing(20)

# 4. Título
titulo = QLabel("Formulário de Cadastro")
titulo.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
titulo.setStyleSheet("""
    font-size: 28px;
    font-weight: bold;
    color: black;
""")
titulo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
layout.addWidget(titulo)

# 5. Campo de entrada
entrada_nome = QLineEdit()
entrada_nome.setPlaceholderText("Digite seu nome completo")
entrada_nome.setMinimumHeight(45)
entrada_nome.setStyleSheet("""
    font-size: 16px;
    color: black;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
""")
entrada_nome.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
layout.addWidget(entrada_nome, alignment=Qt.AlignTop)

# 6. Mensagem de saída
mensagem = QLabel("")
mensagem.setStyleSheet("""
    font-size: 18px;
    color: black;
    padding: 8px;
""")
mensagem.setMinimumHeight(30)
mensagem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
layout.addWidget(mensagem, alignment=Qt.AlignTop)

# 7. Conectar Enter à saudação
entrada_nome.returnPressed.connect(lambda: (
    mensagem.setText(f"Seja bem-vindo, {entrada_nome.text().title()}!"),
    print(f"Nome recebido: {entrada_nome.text().title()}")
))

# 8. Configurar e aplicar layout
janela.setLayout(layout)
janela.show()

# 9. Executar aplicação
app.exec()
