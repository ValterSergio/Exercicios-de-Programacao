from app.funcionario import Funcionario

class Estagiario(Funcionario):
    # tempo de contrato em meses
    def __init__(self, nome, documento, senha_portal, cargo, salario, tempo_contrato: int, salario_fixo: float):
        super().__init__(nome, documento, senha_portal, cargo, salario)
        self._tempo_de_contrato = tempo_contrato
        self.set_salario(salario_fixo)

    def get_tempo_de_contrato(self) -> str:
        return str(self._tempo_de_contrato)
    
    def mostrar_dados(self):
        return f"{super().mostrar_dados()}\nTempo de Contrato: {self.get_tempo_de_contrato()} meses\n{'-'*65}"
    
