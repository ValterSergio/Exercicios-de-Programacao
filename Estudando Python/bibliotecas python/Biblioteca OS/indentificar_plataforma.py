import os
import platform


# indentificação basica da plataforma
def indentificar_plataforma() -> str:
    indentificador = os.name  # uma str

    if indentificador == "nt":  # windowns
        print("Plataforma: WINDOWNS")
    elif indentificador == "posix":  # Unix/Linux/macOS
        print(f"Plataforma: {'Unix/Linux/macOS'.upper()}")
    elif indentificador == "java":  # JVM
        print("Plataforma: JVM JAVA")
    else:
        print(f"Plataforma: {'Desconhecida'.upper()}")

    return indentificador


# indentificação mais precisa
def indentificar_detalhes_plataforma() -> None:
    if hasattr(os, "uname"):
        detalhes = os.uname()
    else:
        detalhes = platform.uname()
    print(f"Sistema: {detalhes.system}")
    print(f"Nome da Máquina: {detalhes.node}")
    print(f"Versão: {detalhes.version}")
    print(f"Release: {detalhes.release}")
    print(f"Arquitetura: {detalhes.machine}")
    print(f"Processador: {detalhes.processor}")


if __name__ == "__main__":
    indentificar_plataforma()
    indentificar_detalhes_plataforma()
