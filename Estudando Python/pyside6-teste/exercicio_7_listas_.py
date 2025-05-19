from PySide6.QtWidgets import (
    QApplication, QWidget, QListWidget, QListWidgetItem,
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton
)
from PySide6 import QtCore
import sys

# Criar o aplicativo
app = QApplication([])

# =======================
# MENU LATERAL ESQUERDO
# =======================

menu_esquerdo = QListWidget()
menu_esquerdo.setMaximumWidth(180)
menu_esquerdo.setStyleSheet("""
    QListWidget {
        background-color: #f0f0f0;
        font-size: 14px;
        color: #222;
        border: 1px solid #ccc;
    }
    QListWidget::item {
        padding: 10px;
    }
    QListWidget::item:selected {
        background-color: #cce5ff;
        color: #000;
    }
""")

# Adicionar itens ao menu
for x in range(15):
    item = QListWidgetItem(f"Opção {x}")
    item.setTextAlignment(QtCore.Qt.AlignLeft)
    menu_esquerdo.addItem(item)

# =========================
# CONTEÚDO PRINCIPAL (CENTRO)
# =========================

texto_principal = QLabel("Seja bem-vindo!")
texto_principal.setAlignment(QtCore.Qt.AlignCenter)
texto_principal.setStyleSheet("font-size: 20px; color: #333; padding: 10px;")

botao_unico = QPushButton("Fechar aplicativo")
botao_unico.setStyleSheet("""
    QPushButton {
        font-size: 28px;
        padding: 8px 16px;
        background-color: black;
        color: white;
        border: none;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: green;
    }
""")
botao_unico.clicked.connect(lambda: sys.exit())

# Layout vertical do conteúdo
layout_conteudo = QVBoxLayout()
layout_conteudo.addStretch()
layout_conteudo.addWidget(texto_principal)
layout_conteudo.addSpacing(10)
layout_conteudo.addWidget(botao_unico, alignment=QtCore.Qt.AlignCenter)
layout_conteudo.addStretch()

# Widget que carrega esse layout
conteudo_principal = QWidget()
conteudo_principal.setLayout(layout_conteudo)

# ========================
# FUNÇÃO DE CLIQUE NO MENU
# ========================
def item_clicado(item: QListWidgetItem):
    texto_principal.setText(f"Você clicou em: {item.text()}")

menu_esquerdo.itemClicked.connect(item_clicado)

# =====================
# JANELA PRINCIPAL
# =====================

# Layout principal horizontal
layout_principal = QHBoxLayout()
layout_principal.setContentsMargins(20, 20, 20, 20)
layout_principal.setSpacing(15)
layout_principal.addWidget(menu_esquerdo)
layout_principal.addWidget(conteudo_principal)

# Widget principal
janela = QWidget()
janela.setLayout(layout_principal)
janela.resize(700, 500)
janela.setWindowTitle("Interface com Menu Lateral")
janela.setStyleSheet("background-color: white;")
janela.show()

# Executar aplicativo
app.exec()
