from pathlib import Path

class MenuController:
    # recebe a opção do usuario e valida o resultado
    def validar_escolha(self, escolha: str) -> dict:
        # escolha é um numero?
        numerico = escolha.isdigit()
        if not numerico:
            erro = f"ERRO: Informe apenas números inteiros.\nValor Informado: {escolha}"
            caminho = __file__
            return {
                "mensagem": False,
                "resposta": erro,
                "caminho": caminho,
                "objeto": self.__class__.__name__,
                "metodo": "validar_escolha"
                }
        
        
        # podemos afirmar que a string é um número inteiro
        num = int(escolha)
        if not (num >= 1 and num <= 4):
            erro = f"ERRO: Informe apenas números no intervalo de 1 a 4.\nValor informado: {escolha}"
                
            return {
                "mensagem": False,
                "resposta": erro,
                "caminho": __file__,
                "objeto": self.__class__.__name__,
                "metodo": "validar_escolha"
            }

        return {
            "mensagem": True,
            "resposta": num,
            "caminho": __file__,
            "objeto": self.__class__.__name__,
            "metodo": "validar_escolha"
        }