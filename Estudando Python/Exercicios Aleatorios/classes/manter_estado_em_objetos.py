class Camera:
    def __init__(self, modelo):
        self.modelo = modelo
        self.filmando = False
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            print("Ligando camera..")
            self.ligado = True
            return
    
        print("Camera já está ligada")
        return 
    
    def desligar(self):
        if self.filmando:
            print("Camera filmando, para de filmar antes por favor")
            return
        
        if self.ligado:
            print("Desligando camera")
            self.ligado = False
            return 


    def filmar(self):
        if not self.ligado:
            print("Camera desligada, impossivel filmar")
            return 

        if not self.filmando:
            print("Camera Filmando")
            self.filmando = True
            return
        
        print("Camera já está gravando")
        return

    def parar_filmagem(self):
        if self.filmando:
            print("Encerrando filmagem")
            self.filmando = False
            return
        
        print("Camera não está gravando agora")
        return 
        

if __name__ == "__main__":
    c = Camera("Sony")
    c.ligar()
    c.filmar()
    c.parar_filmagem()
    c.desligar()
