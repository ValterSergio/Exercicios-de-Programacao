from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Qt
import sys

class BotaoDeGasto(QPushButton):
    def __init__(self):
        super().__init__("Adicionar despesa")
        # Habilita o rastreamento do mouse (por padrão, só move com botão pressionado)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        print("Mouse está se movendo sobre o botão")
        # Chame o comportamento padrão (opcional)
        # super().mouseMoveEvent(event)

app = QApplication(sys.argv)

b1 = BotaoDeGasto()
b1.resize(200, 50)
b1.show()

app.exec()
