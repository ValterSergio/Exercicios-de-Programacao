from datetime import datetime


class Fatura:
    """
    Representa uma fatura a pagar com informações sobre o serviço,
    valor, data de vencimento, status de pagamento e atraso.
    """

    def __init__(self, servico: str, valor: int, vencimento: datetime):
        self.vencimento = vencimento
        self.servico = servico.lower()
        self.atrasada = False
        self.quitada = False
        self.valor = valor

    def __str__(self):
        return (
            f"{'-'*60}\n"
            f"Fatura: {self.servico}\tMês: {self.vencimento.month}\n"
            f"{'-'*60}\n"
            f"Valor: {self.valor:,.2f}\n"
            f"Vencimento: {self.vencimento.strftime('%d/%m/%Y')}\n"
            f"Status: {'Atrasada' if self.atrasada else 'Em Dia'}\n"
            f"Conta {'Quitada' if self.quitada else 'Para Pagar'}\n"
            f"{'-'*60}"
            )


    def quitar_fatura(self):
        self.quitada = True
        if self.quitada:
            print("conta paga")
            return True

    def verificar_atraso(self):
        self.atrasada =  (datetime.now().date() > self.vencimento.date()) if not self.quitada else True

    def para_dicionario(self):
        return {
            "servico": self.servico,
            "valor": self.valor,
            "vencimento": self.vencimento.strftime("%d/%m/%Y"),
            "quitada": self.quitada,

        }
    
    @staticmethod
    def de_dicionario(dados):
        vencimento = datetime.strptime(dados['vencimento'], "%d/%m/%Y")
        fatura = Fatura(dados["servico"], dados['valor'], vencimento)
        fatura.quitada = dados['quitada']
        return fatura

if __name__ == "__main__":
    fatura = "agua"
    valor = 10
    data = datetime(2025, 4, 13)
    fatura_agua = Fatura(fatura, valor, data)
    # fatura_agua.quitar_fatura()
    print(fatura_agua)


