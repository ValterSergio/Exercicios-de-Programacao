from mutagen.mp3 import MP3
import pygame

def validar_pasta(nome: str) -> bool:
    nomes_proibidos = ["meus programas", "microsoft", "app", ".gradle", ".vscode", ".wdm", ".m2", ".cache",  ".virtualbox", "virtualbox", "git", ".git"]
    for palavra in nomes_proibidos:
        if palavra in nome.lower():
            return False
    return True

def converter_segundos(total):
    
    horas = total // 3600
    minutos = (total % 3600) // 60
    segundos = total % 60

    return f" {int(horas)}:{int(minutos)}:{int(segundos)}"

def obter_duracao(caminho):
    audio = MP3(caminho)
    total = audio.info.length
    return int(total)

def executar_musica(caminho: str):
    esta_tocando = musica_esta_tocando(caminho)
    if not esta_tocando:
        pygame.mixer.init()
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()

def musica_esta_tocando(caminho: str) -> bool:
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    return pygame.mixer.get_busy()

def pausar_musica(caminho: str):
    esta_tocando = musica_esta_tocando(caminho)
    if esta_tocando:
        pygame.mixer.init()
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.pause()
