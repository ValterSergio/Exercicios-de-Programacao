import sys

def log_com_stdout(func, msg):
    # redirecionando a saida do console para um arquivo
    sys.stdout = open('saida_do_console.txt', 'w')

    print("Adicionando registro:\n")
    func(msg)

    print("\nRegistro feito com sucesso")

    sys.stdout.close()  # Fecha o arquivo

if __name__ == "__main__":
    msg = "Este texto vai para o arquivo 'saida_do_console.txt'."
    log_com_stdout(print, msg)