from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout
)
import sys

app = QApplication(sys.argv)

# iniciar janela principal
janela_principal = QMainWindow()
janela_principal.setWindowTitle("Valter")

# Criar um central widget
central_widget = QWidget()

# Criar um layout
layout = QHBoxLayout()

# Criar um botão
botao1 = QPushButton("Eu sou o botao1")
botao1.setStyleSheet("color: green;")
botao1.setFont("arial")

# adicionar o botão dentro do layout
layout.addWidget(botao1)

# adicionar o layout dentro do central widget
central_widget.setLayout(layout)

# adiciona o central widget dentro da janela principal
janela_principal.setCentralWidget(central_widget)

janela_principal.show()
app.exec()