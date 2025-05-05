from pathlib import Path
import json

CAMINHO_SALVAR = Path(__file__).parent / "Classe_salva.json"

class Qualquer:
    def __init__(self):
        self.um = 1
        self.dois = 2
        self.tres = 3


if __name__ == "__main__":
    teste = Qualquer()
    teste.__dict__["quatro"] = 4
    
    # salvando classe
    with open(CAMINHO_SALVAR, "w", encoding="utf-8") as classe:
        json.dump(vars(teste), classe, ensure_ascii=False, indent=2)

