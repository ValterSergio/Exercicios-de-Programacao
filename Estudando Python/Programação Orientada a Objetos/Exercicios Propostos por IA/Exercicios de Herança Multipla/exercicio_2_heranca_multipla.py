class Ave:
    def voar(self):
        print(f"{self.__class__.__name__} está voando")

class Peixe:
    def nadar(self):
        print(f"{self.__class__.__name__} está nadando")

class Pinguim(Ave, Peixe):
    def voar(self): # sobrescrita de método
        print(f"{self.__class__.__name__} não sabe voar")
        

if __name__ == "__main__":
    pinguim = Pinguim()
    pinguim.voar()
    pinguim.nadar()