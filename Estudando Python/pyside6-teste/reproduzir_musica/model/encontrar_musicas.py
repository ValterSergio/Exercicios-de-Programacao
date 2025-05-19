import os
from .auxiliares import obter_duracao, converter_segundos, validar_pasta
from reproduzir_musica.model.dados import RegistrarMusicas

def filtrar_por_extensao(caminho: str=None, extensao_alvo: str=".mp3"):
    if caminho is None:
        # iniciar loop da pasta raiz C:\Users\name_user
        caminho = os.environ["USERPROFILE"]
    
    musicas_salvas = []
    for nome_pasta_atual, subpasta, arquivos in os.walk(caminho):

        if not validar_pasta(nome_pasta_atual):
            continue

        for i in arquivos:
            caminho_arquivo = os.path.abspath(os.path.join(nome_pasta_atual, i))
            caminho, extensao = os.path.splitext(caminho_arquivo)
            if extensao == extensao_alvo:
                musicas_salvas.append(caminho_arquivo)
    return musicas_salvas

def filtrar_arquivos_mp3(tempo_minimo: int=30) -> list:
    musicas = RegistrarMusicas()

    for caminho in filtrar_por_extensao():
        if int(obter_duracao(caminho)) >= tempo_minimo: # 30 segundos não deve ser musica
            musica = {
                "nome": caminho.split("\\")[-1:][0][:-4],
                "caminho": caminho,
                "duracao": converter_segundos(obter_duracao(caminho))
            }
            musicas.adicionar_musica(**musica)
    return musicas


# if __name__ == "__main__":
#     resultado = filtrar_arquivos_mp3(tempo_minimo=5)
#     print(f"Musicas encontradas (total): ", len(resultado))
#     print(f"Musicas encontradas: ", resultado)
    