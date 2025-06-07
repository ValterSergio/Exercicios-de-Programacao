from PySide6.QtWidgets import (
    QFormLayout, QApplication, QVBoxLayout, QWidget,
    QLineEdit, QPushButton, QLabel
)


def somar():
    try:
        valor1 = float(numero1.text())
        valor2 = float(numero2.text())
        resultado = valor1 + valor2
        resultado_label.setText(f"Resultado: {resultado}")
    except ValueError:
        resultado_label.setText("Por favor, digite números válidos.")


app = QApplication([])

# Layouts
form_layout = QFormLayout()
layout_principal = QVBoxLayout()

# Campos de entrada
numero1 = QLineEdit()
numero2 = QLineEdit()

form_layout.addRow("Digite um Número:", numero1)
form_layout.addRow("Digite outro Número:", numero2)

# Botão
botao = QPushButton("Somar")
botao.clicked.connect(somar)

# Resultado
resultado_label = QLabel("Resultado: ")

# Monta layout principal
layout_principal.addLayout(form_layout)
layout_principal.addWidget(botao)
layout_principal.addWidget(resultado_label)

# Widget principal
widget_principal = QWidget()
widget_principal.setLayout(layout_principal)
widget_principal.setWindowTitle("Somador")
widget_principal.resize(300, 150)
widget_principal.show()

app.exec()
