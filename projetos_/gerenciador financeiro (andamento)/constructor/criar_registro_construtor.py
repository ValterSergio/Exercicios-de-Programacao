from view.criar_registro_view import CriarRegistroView
from controller.criar_registro_controller import CriarRegistroController
from model.repositorio import Repositorio

from util.limpar_terminal import limpar_terminal

class CriarRegistroConstructor:
    def criar_registro(self):
        self.view = CriarRegistroView()
        self.controller = CriarRegistroController()
        self.repositorio = Repositorio()
        
        while True:
            # obtem a operação 
            limpar_terminal()
            operacao = self.obter_operacao_constructor()
            if isinstance(operacao, bool):
                break

            # obtem a categoria do registro
            limpar_terminal()
            categoria = self.obter_categoria_constructor(operacao)
            if isinstance(categoria, bool):
                break

            # obtem uma descrição 
            limpar_terminal()
            descricao = self.obter_descricao_construtor()
    
            # obtem a data do registro
            limpar_terminal()
            data = self.obter_data_constructor()

            # obtem o valor do registro
            limpar_terminal()
            valor = self.obter_valor_constructor()
          
            try:
                # salvar o registro no repositorio

                limpar_terminal()
                self.repositorio.salvar_registro(operacao, categoria, descricao, data, valor)
                self.view.criar_registro_sucesso_view()
                return # encerra a criação total do registro
            except Exception as erro:
                limpar_terminal()
                self.view.obter_falha_view(str(erro))
                print("\nTente Novamente !!\n")
                continue
            
        limpar_terminal()
        print("\nOperação Cancelada !!!\n")

    # métodos comuns
    def cancelar_operacao(self, resposta: str):
    
        # se a resposta do controller for "cancelada" então pode quebrar o laço
        if resposta == 'cancelada':
            limpar_terminal()
            print("Operação Cancelada")
            return True
        return False

    def obter_descricao_construtor(self) -> str:
        while True:
            resposta_usuario = self.view.obter_descricao_view()
            resposta_controller = self.controller.validar_descricao(resposta_usuario)

            mensagem = resposta_controller['mensagem']
            resposta = resposta_controller['resposta']

            if mensagem:
                self.view.obter_descricao_sucesso_view()
                return resposta

            limpar_terminal()
            print("\n Aviso Sai do laço apenas quando a opção correta for selecionada \n")
            self.view.obter_falha_view(resposta)

    def obter_categoria_constructor(self, operacao: str) -> str|bool:
        while True:
            # filtrando as categorias por operação
            if operacao == "entrada":
                repositorio = ["salario", "vendas"]
            elif operacao == "saida":
                repositorio = ["mercado", "casa", "transporte", "higiene"]
            
            # entrada
            resposta_usuario = self.view.obter_categoria_view(repositorio)
            resposta_controller = self.controller.validar_categoria(repositorio, resposta_usuario)

            # processar resultado
            mensagem = resposta_controller["mensagem"]
            resposta = resposta_controller["resposta"]

            # verificar se foi cancelada
            if self.cancelar_operacao(resposta):
                return False
            
            if mensagem:
                limpar_terminal()
                self.view.obter_operacao_sucesso_view()
                return resposta

            limpar_terminal()
            print("\n Aviso Sai do laço apenas quando a opção correta for selecionada \n")
            self.view.obter_falha_view(resposta)

    def obter_operacao_constructor(self) -> str|bool:
        while  True:
            resposta_usuario = self.view.obter_operacao_view()
            resposta_controller = self.controller.validar_operacao(resposta_usuario)
            
            if resposta_controller['mensagem']:
                limpar_terminal()
                self.view.obter_operacao_sucesso_view()
                return resposta_controller['resposta'] # retorna uma string

            # se a resposta do controller for "cancelada" então pode quebrar o laço
            if self.cancelar_operacao(resposta_controller["resposta"]):
                return False
                

            limpar_terminal()
            print("\n Aviso Sai do laço apenas quando a opção correta for selecionada \n")
            self.view.obter_falha_view(resposta_controller['resposta'])

    def obter_data_constructor(self) -> str:
        while True:
            resposta_usuario = self.view.obter_data_view()
            resposta_controller = self.controller.validar_data(resposta_usuario)

            mensagem = resposta_controller['mensagem']
            resposta = resposta_controller['resposta']

            if mensagem:
                self.view.obter_data_sucesso_view()
                return resposta
            
            limpar_terminal()
            print("\n Aviso Sai do laço apenas quando uma hora válida for passada \n")
            self.view.obter_falha_view(resposta)

    def obter_valor_constructor(self) -> float:
            while True:
                resposta_usuario = self.view.obter_valor_view()
                resposta_controller = self.controller.validar_valor(resposta_usuario)

                mensagem = resposta_controller['mensagem']
                resposta = resposta_controller['resposta']

                if mensagem:
                    self.view.obter_valor_sucesso_view()
                    return resposta
                
                limpar_terminal()
                print("\n Aviso Sai do laço apenas quando um valor válido for passado !!! \n")
                self.view.obter_falha_view(resposta)