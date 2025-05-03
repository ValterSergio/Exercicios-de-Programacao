from app.funcionario import Funcionario

class Terceirizado(Funcionario):
    def __init__(self, nome, documento, senha_portal, cargo, salario, empresa: str):
        super().__init__(nome, documento, senha_portal, cargo, salario)
        self._empresa = empresa

    def get_empresa(self) -> str:
        return self._empresa
    
    def mostrar_dados(self):
        return f"{super().mostrar_dados()}\nTerceirizado: {self.get_empresa()}\n{"-"*65}"