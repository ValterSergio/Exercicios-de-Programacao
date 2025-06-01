from abc import ABC, abstractmethod

class Autentificacao(ABC):
    @abstractmethod
    def autentificar(self, credencial):
        pass

class Administrador(Autentificacao):
    def autentificar(self, credencial):
        return credencial == "valter"

class Cliente(Autentificacao):
    def autentificar(self, credencial):
        return credencial == "cliente"


print(Cliente().autentificar("cliente"))
print(Administrador().autentificar("valter"))