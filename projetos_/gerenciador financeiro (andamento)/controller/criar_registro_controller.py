from datetime import datetime

class CriarRegistroController:
    def validar_operacao(self, operacao: str) -> dict:
        # verifica se é um número
        numerico = operacao.isdigit()
        if not numerico:
            erro = f"ERRO: Informe apenas números inteiros.\nValor Informado: {operacao}"
            caminho = __file__
            return {
                "mensagem": False,
                "resposta": erro,
                "caminho": caminho,
                "objeto": self.__class__.__name__,
                "metodo": "validar_operacao"
                }

        # verifica se a escolha é 1 ou 2         
        escolha = int(operacao)
        if escolha not in (1, 2, 3):
            erro = f"ERRO: Informe apenas 1 ou 2.\nValor Informado: {escolha}"
            caminho = __file__
            return {
                "mensagem": False,
                "resposta": erro,
                "caminho": caminho,
                "objeto": self.__class__.__name__,
                "metodo": "validar_operacao"
                }
        
        match escolha:
            case 1:
                resposta = "entrada"
            case 2:
                resposta = "saida"
            case 3:
                resposta = "cancelada"
                return {
                        "mensagem": False,
                        "resposta": resposta,
                        "caminho": __file__,
                        "objeto": self.__class__.__name__,
                        "metodo": "validar_operacao"
                        }
        
    
        return {
                "mensagem": True,
                "resposta": resposta,
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_operacao"
                }
    
    def validar_categoria(self, categorias: list[str], categoria: str) -> dict:
        
        # categoria deve ser um numero inteiro
        if not categoria.isdigit():
            erro = f"Informe apenas numeros inteiros.\nValor informado: {categoria}"
            return {
                "mensagem": False,
                "resposta": erro,
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_categoria"
            }
        
        # se esse número for 0 cancela a operação
        if categoria == "0":
            return {
                "mensagem": False,
                "resposta": "cancelada",
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_categoria"
            }
        
        # se o numero for menor que o total de items + 1 a categoria esta fora do intervalo
        total_categorias = len(categorias) + 1 # estou usando 0 para cancelar e incrementei a lista para marcar do 1 
        categoria = int(categoria)
        if categoria > total_categorias:
            erro = f"ERRO: Escolha fora do intervalo de categorias, informe um número dentro do limite.\nValor informado: {categoria} Limite: {total_categorias}."
            return {
                "mensagem": False,
                "resposta": erro,
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_categoria"
            }

        # até aqui categoria é um número inteiro dentro do intervalo
        categoria_selecionada = categorias[categoria - 1] # -1 para compensar o incremento no indice
        return {
            "mensagem": True,
            "resposta": categoria_selecionada,
            "caminho": __file__,
            "objeto": self.__class__.__name__,
            "metodo": "validar_categoria"
        }
            
    def validar_descricao(self, descricao: str) -> dict:
        # elimina os espaços em excesso
        descricao = descricao.strip()

        # verifica se é maior que o limite permitido de 200 caracteres
        if len(descricao) > 200:
            erro = f"ERRO: Limite de caracteres excedido - limite de 200.\nTotal de caracteres registrados: {len(descricao)}"
            return {
                "mensagem": False,
                "resposta": erro,
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_descricao"
            }
        
        # verifica se está vazio - remove todos os espaços em branco 
        if len(descricao.replace(" ", "")) == 0:
            descricao = "Descrição não informada"
        
        return {
                "mensagem": True,
                "resposta": descricao,
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_descricao"
            }
    
    def validar_data(self, data: str) -> dict:
        formato = "%d/%m/%Y"
        try:
            datetime.strptime(data, formato)
            return {
                "mensagem": True,
                "resposta": data,
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_data"
            }
        except Exception as erro:
            return {
                "mensagem": False,
                "resposta": str(erro),
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_data"
            }

    def validar_valor(self, valor: str) -> dict:
        try:
            valor_real = float(valor)
        except Exception as erro:
            return {
                "mensagem": False,
                "resposta": str(erro),
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_valor"
            }
        
        if valor_real < 0:
            return {
                "mensagem": False,
                "resposta": f"ERRO: Informe apenas valores positivos.\nValor informado: {valor}.\n",
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_valor"
            }
        
        return {
            "mensagem": True,
            "resposta": valor_real,
            "caminho": __file__,
            "objeto": self.__class__.__name__,
            "metodo": "validar_valor"
        }
    
