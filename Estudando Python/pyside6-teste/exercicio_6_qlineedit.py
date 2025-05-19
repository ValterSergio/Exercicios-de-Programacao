from PySide6.QtWidgets import (
    QApplication, QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout, QSizePolicy
)

class JanelaBase(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulário Simples")
        self.resize(600, 300)
        self.setStyleSheet("background-color: #f2f2f2; padding: 20px;")

    def adicionar_layout(self, layout: QVBoxLayout):
        self.setLayout(layout)


class LayoutBase(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setSpacing(15)
        self.setContentsMargins(10, 10, 10, 10)

    def adicionar_widget(self, widget: QWidget):
        self.addWidget(widget)


class TextoPerguntar(QLabel):
    def __init__(self, texto: str):
        super().__init__(texto.strip().capitalize())
        self.setStyleSheet("color: #333; font-size: 20px;")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)


class ReceberEntrada(QLineEdit):
    def __init__(self, placeholder: str):
        super().__init__()
        self.setPlaceholderText(placeholder.capitalize())
        self.setStyleSheet("color: red; font-size: 16px; padding: 5px;")
        self.setMinimumHeight(30)


app = QApplication([])

# criar componentes
janela = JanelaBase()
layout = LayoutBase()
texto = TextoPerguntar("Qual o seu nome?")
entrada = ReceberEntrada("digite aqui seu nome")

mensagem = QLabel("")
mensagem.setStyleSheet("font-size: 18px; color: green;")

# ação ao pressionar Enter
entrada.returnPressed.connect(lambda: mensagem.setText(f"Bem vindo, {entrada.text().title()}"))

# adicionar ao layout
layout.adicionar_widget(texto)
layout.adicionar_widget(entrada)
layout.adicionar_widget(mensagem)
janela.adicionar_layout(layout)

# exibir
janela.show()
app.exec()
