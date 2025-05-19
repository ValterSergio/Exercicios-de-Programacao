from reproduzir_musica.view.lista_de_musicas import lista_de_musicas2
from reproduzir_musica.view.coluna_central import coluna_central
from reproduzir_musica.model.encontrar_musicas import filtrar_arquivos_mp3
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

app = QApplication([])

# layouts
coluna_esuerda_musica = lista_de_musicas2()
coluna_direita = coluna_central()
layout = QHBoxLayout()
layout.addWidget(coluna_esuerda_musica)
layout.addWidget(coluna_direita)

# widget central
widget_central = QWidget()
widget_central.setLayout(layout)
widget_central.show()

# executar
app.exec()
