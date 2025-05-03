""" MRO """

class A:
    def printar(self): print(f"Executando {self.__class__.__name__} - A")

class B:
    def printar(self): print(f"Executando {self.__class__.__name__} - B")

class C(A, B): pass # sempre começa da esquerda para direita


if __name__ == "__main__":
    C().printar() # Classe C - Executa metodo da Classe A
    
    class C(B, A): pass # apenas para visualização
    C().printar() # Classe C - Executa metodo da Classe B