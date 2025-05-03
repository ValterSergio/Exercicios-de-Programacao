import os
import sys

# Adiciona o diretório pai ao sys.path para permitir a importação de módulos da pasta 'app'
pasta_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_pai)

from app.terceirizado import Terceirizado
from ferramentas.funcoes_auxiliares import gerador_de_cpf

if __name__ == "__main__":

    t = Terceirizado("after", gerador_de_cpf(), "12345", "Ajudante de cozinha", 1879.69, "Terceirizada name's")
    print(t.mostrar_dados())