import json
import os
from reproduzir_musica.model.auxiliares import executar_musica, pausar_musica

def obter_caminho() -> str:
    return os.path.join(os.path.dirname(__file__), 'registros_json')

def formar_nome(nome1, nome2):
    return os.path.join(nome1, nome2)

class RegistrarMusicas:
    def __init__(self):
        self.caminho_raiz = obter_caminho()
        os.makedirs(self.caminho_raiz, exist_ok=True)
        self.lista_de_musicas = self.carregar_arquivo()

    def carregar_arquivo(self):
        caminho_arquivo = formar_nome(self.caminho_raiz, "registroMusicas.json")
        # Se o arquivo não existir, cria um JSON vazio
        if not os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
                json.dump([], arquivo)
            return []
        
        # Se o arquivo existir, carrega os dados
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return [Musica(**item) for item in dados]

    def salvar_arquivo(self):
        caminho_arquivo = formar_nome(self.caminho_raiz, "registroMusicas.json")
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump([musica.__dict__ for musica in self.lista_de_musicas], arquivo, ensure_ascii=False, indent=2)
    
    

    def adicionar_musica(self, **kwargs):
        self.lista_de_musicas.append(Musica(**kwargs))
        self.salvar_arquivo()

class Musica:
    def __init__(self, nome, caminho, duracao):
        self.nome = nome
        self.caminho = caminho
        self.duracao = duracao
    
    def get_nome_musica(self):
        return self.nome
    
    def get_caminho_musica(self):
        return self.caminho
    
    def get_duracao(self):
        return self.duracao
    
    def reproduzir_musica(self):
        executar_musica(self.caminho)
    
    def parar_musica(self):
        pausar_musica(self.caminho)
