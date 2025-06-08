import sys
import dis
def estudando_sys_exc_info():
    try:
        dividir = 5 / 0
    except Exception:
        tipo, valor, rastreamento = sys.exc_info()
        print(f'Tipo de Erro: ', tipo.__name__)
        print(f'Causa do erro: ',str(valor))
        print(f'Linha de erro: ', rastreamento.tb_lineno)
        print(f'Ultima instrução executada no bytecode do python: ', rastreamento.tb_frame.f_lasti)

def inspecionar_bytecode(func):
    dis.dis(func)

if __name__ == "__main__":
    print("\nTrabalhando execeções com sys.exc_info()\n")
    estudando_sys_exc_info()
    print("\nExibindo o o bytecode para melhor entender f_lasti\n")
    inspecionar_bytecode(estudando_sys_exc_info)