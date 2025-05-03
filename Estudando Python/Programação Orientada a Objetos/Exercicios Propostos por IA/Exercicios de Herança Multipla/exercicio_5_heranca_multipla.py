class Impressora:
    def imprimir(self): print("Imprimindo...")

class Scanner:
    def escanear(self): print("Escaneando...")

# Composição 
class Multifuncional:
    def __init__(self):
        self.impressora = Impressora()
        self.scanner = Scanner()
    
    def imprimir(self): self.impressora.imprimir()
    def escanear(self): self.scanner.escanear()
