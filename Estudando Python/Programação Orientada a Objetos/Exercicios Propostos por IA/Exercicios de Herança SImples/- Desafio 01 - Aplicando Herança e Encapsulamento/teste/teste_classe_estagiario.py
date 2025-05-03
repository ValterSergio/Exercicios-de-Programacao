import os
import sys

# Adiciona o diretório pai ao sys.path para permitir a importação de módulos da pasta 'app'
pasta_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_pai)

from app.estagiario import Estagiario
from ferramentas.funcoes_auxiliares import gerador_de_cpf

def testar_classe_estagiario():
    e = Estagiario("tioter", gerador_de_cpf(), "1234567", "Cozinheiro chefe", 0, 6, 2456.65)

    print(e.mostrar_dados())
    print()
    print("Brincando com alguns metodos")
    print(e.get_tempo_de_contrato())
    print(e.set_documento(gerador_de_cpf()))
    print(e.set_cargo("Chefe de Cozinha"))
    print(e.mostrar_dados())

    
if __name__ == "__main__":
    testar_classe_estagiario()