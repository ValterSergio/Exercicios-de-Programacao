import sys
from time import sleep

def sair_do_programa():
    print("\nSaindo do programa...")
    for x in range(100):
        if x == 10:
            # podemos sair do programa diretamente com exit em caso de erro
            sys.exit("A contagem acabou.")
        sleep(0.5)
        print("contador: ", x)

def controlar_recursao(limite):
    sys.setrecursionlimit(limite)

def recursao(n):
    if n > 0:
        print("Recursão: ", n)
        sleep(0.5)
        return recursao(n-1)
    else:
        return 'fim'

if __name__ == "__main__":
    import os
    limite = 10 - 2 # 2 representa o teto que não se deve invadir
    controlar_recursao(10)
    recursao(limite)
    print("recursão concluida")
    os.system('cls') # para limpar terminal
    sair_do_programa()