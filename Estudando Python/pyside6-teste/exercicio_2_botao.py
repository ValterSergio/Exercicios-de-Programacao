from PySide6.QtWidgets import QApplication, QPushButton
from sys import argv
"""
-- modelo com o unico botão
-- objetivo estudar a classe PushButton
-- Aprender a moldar um PushButton livremente
-- Realizar ações com PushButton

--------- exemplo inicial para criação de botão

-- primeiro se deve instanciar QApplication 
-- passar uma lista com os argumentos de linha de comando 
----- se não usar argumentos de linha de comando
-------- passar uma lista vazia 
app = QApplication(argv)


botao = QPushButton("Imprimir botão único")
botao.show()

app.exec()
"""

app = QApplication(argv)
botao = QPushButton("Olá mundo")
botao.show()
app.exec()
