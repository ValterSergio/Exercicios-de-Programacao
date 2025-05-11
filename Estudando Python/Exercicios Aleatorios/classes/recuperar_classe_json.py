if __name__ == "__main__":
    import json
    import os
    from salvar_classe_json import CAMINHO_SALVAR, Qualquer


    # carregando dados
    with open(CAMINHO_SALVAR, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    
    # instanciando objeto
    carregar_classe = Qualquer()
    print(carregar_classe.__dict__)

    # recriando o estado do objeto
    carregar_classe.__dict__.update(dados)
    print(carregar_classe.__dict__)
    
    # apagando arquivo de teste
    os.remove(CAMINHO_SALVAR)