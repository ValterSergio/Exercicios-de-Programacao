import sys

# Ver os argumentos passados na linha de comando
def soma(x, y):
    return x + y

def checar_argumentos():
    if len(sys.argv) <= 1:
        print('passe argumentos na linha de comando')
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        print("A soma dos argumentos passado na linha de comando é : ", soma(x, y))

def caminho_do_arquivo():
    print("\nExibindo caminho do arquivo: ")
    return sys.argv[0]
if __name__ == "__main__":
    
    print("Este programa deve ser executado apenas com a linha de comando do terminal\n")
    
    print("Passe dois numeros para soma")
    
    print("Python argumento_na_linha_de_comando.py 5 5")
    
    print("\nVocê verá o resultado no terminal\n")
    
    print("CHECANDO ARGUMENTOS\n")

    checar_argumentos()
    print(caminho_do_arquivo())
    print("\nFIM")