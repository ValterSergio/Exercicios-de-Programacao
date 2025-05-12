class FiltroDeFaturas:
    
    @staticmethod
    def por_mes(faturas: list[object], mes: int) -> list:
        return [fatura for fatura in faturas if fatura.vencimento.month == mes]
    
    @staticmethod
    def atrasadas(faturas: list[object]) -> list:
        lista = []
        for fatura in faturas:
            fatura.verificar_atraso()
            if fatura.atrasada:
                lista.append(fatura)
        return lista

    @staticmethod
    def por_servico(faturas: list[object], servico: str) -> list:
        return [fatura for fatura in faturas if fatura.servico == servico]
    
    @staticmethod
    def contas_pagas(faturas: list[object]) -> list:
        return [fatura for fatura in faturas if fatura.quitada]
    