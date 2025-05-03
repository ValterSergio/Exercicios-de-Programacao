class A:
    def printar(self):
        print("Método da Classe A")
        super().printar()

class B:
    def printar(self):
        print("Método da Classe B")
        super().printar()

class C(A, B):
    def printar(self):
        print("Método da Classe C")
        super().printar()
    
class Base:
    def printar(self): print("Classe Base, que não Herda de Ninguem")

class Final(C, Base): pass

Final().printar()