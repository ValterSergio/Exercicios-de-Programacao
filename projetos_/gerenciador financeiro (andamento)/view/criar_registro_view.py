
class CriarRegistroView:
    def obter_operacao_view(self) -> str:
        print("-"*65)
        print("\n\t\tInformar Operação de Registro\n")
        print("-"*65)
        print("1. Operação de entrada")
        print("2. Operação de saída")
        print("3. Cancelar Registro")
        print("-"*65)
        escolha = input("Escolha uma opção: ")
        print("-"*65)
        return escolha
    
    def obter_falha_view(self, mensagem: str):
        print("-"*65)
        print("\nERRO ENCONTRADO !!!\n")
        print("-"*65)
        print(mensagem.capitalize())
        print("-"*65)
    
    def obter_operacao_sucesso_view(self):
        print("-"*65)
        print("\nOperação anotada com sucesso !!!\n")
        print("-"*65)
    
    def obter_categoria_view(self, categorias: list[str]):
        print("-"*65)
        print("\nCategorias Registradas\n")
        print("-"*65)
        indice = 0
        print(f"PARA CANCELAR DIGITE: {indice}  ")
        for categoria in categorias:
            indice += 1
            print(f"Indice: {indice} - Categoria: {categoria}")

        print("-"*65)
        escolha = input("Escolha uma categoria: ")
        print("-"*65)
        return escolha
    
    def obter_categoria_sucesso_view(self):
        print("-"*65)
        print("\nCategoria anotada com sucesso!!! \n")
        print("-"*65)
    
    def obter_descricao_view(self):
        print("-"*65)
        print("\nFaça uma breve descrição sobre a operação\n")
        print("-"*65)
        escolha = input("Escreva aqui: ")
        print("-"*65)
        return escolha
    
    def obter_descricao_sucesso_view(self):
        print("-"*65)
        print("\nDescrição anotada com sucesso !!!\n")
        print("-"*65)
    
    def obter_data_view(self):
        print("-"*65)
        print("\nInforme a data da operação\n")
        print("-"*65)
        escolha = input("Informe a data no formato DD/MM/AAAA: ")
        print("-"*65)
        return escolha
    
    def obter_data_sucesso_view(self):
        print("-"*65)
        print("\nData anotada com sucesso !!!\n")
        print("-"*65)

    def obter_valor_view(self):
        print("-"*65)
        print("\nInforme o valor da operação (apenas números positivos) !!!\n")
        print("-"*65)
        escolha = input("Informe o o valor: ")
        print("-"*65)
        return escolha
    
    def obter_valor_sucesso_view(self):
        print("-"*65)
        print("\nValor anotado com sucesso !!!\n")
        print("-"*65)

    def criar_registro_sucesso_view(self):
        print("-"*65)
        print("\nRegistro Criado com sucesso !!!\n")
        print("-"*65)
