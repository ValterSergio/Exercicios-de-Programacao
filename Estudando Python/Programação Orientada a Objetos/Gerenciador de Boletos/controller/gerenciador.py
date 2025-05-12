from model.fatura import Fatura
from model.filtros import FiltroDeFaturas
from datetime import datetime

class GerenciadorFaturas:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.faturas = self.repositorio.carregar_arquivo()
        self.filtro = FiltroDeFaturas()

    def adicionar_fatura(self, servico, valor, vencimento_str):
        vencimento = datetime.strptime(vencimento_str, "%d/%m/%Y")
        nova = [fatura for fatura in self.faturas if fatura.servico == servico and fatura.vencimento.month == vencimento.month]
        if nova:
            print("Fatura já existe para esse mês.")
            return
        self.faturas.append(Fatura(servico, valor, vencimento))
        self.repositorio.salvar_arquivo(self.faturas)
        
    def listar_faturas(self):
        return self.faturas
    
    def quitar_fatura(self, servico, mes: int):
        for fatura in self.faturas:
            if fatura.servico == servico.lower() and fatura.vencimento.month == mes:
                fatura.quitar()
                self.repositorio.salvar(self.faturas)
                print("Fatura quitada com sucesso.")
                return
        print("Fatura não encontrada.")

    def listar_faturas_por_mes(self, mes: int) -> list[Fatura]:
        return self.filtro.por_mes(self.faturas, mes)
    
    def listar_faturas_por_servico(self, servico: str) -> list[Fatura]:
        return self.filtro.por_servico(self.faturas, servico)
    
    def listar_faturas_pagas(self) -> list[Fatura]:
        return self.filtro.contas_pagas(self.faturas)

    def listar_faturas_atrasadas(self):
        return self.filtro.atrasadas(self.faturas)
             