from os import path, makedirs
import json
from model.fatura import Fatura

CAMINHO = path.join("dados", "registroFaturas.json")

class RepositorioJSON:
    def __init__(self, caminho=CAMINHO):
        self.caminho = caminho
        makedirs(path.dirname(caminho), exist_ok=True)
    
    def carregar_arquivo(self):
        if not path.exists(self.caminho):
            return []
        
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                return []
            
            try:
                dados = json.loads(conteudo)
                return [Fatura.de_dicionario(dado) for dado in dados]
            except Exception as erro:
                print(f"Erro: {str(erro)}")


    def salvar_arquivo(self, faturas):
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump([f.para_dicionario() for f in faturas], arquivo, indent=2, ensure_ascii=False)