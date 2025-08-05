from src.views.buscar_pessoas_view import BuscarPessoaView
from src.controller.buscar_pessoa_controller import BuscarPessoaController
from src.models.repositorio.repositorio_pessoa import RepositorioPessoas


def buscar_pessoa_construtor(repositorio: RepositorioPessoas):
    buscar_pessoa_view = BuscarPessoaView()
    buscar_pessoa_controller = BuscarPessoaController()
    # exibe a interface de busca e coleta a informação do usuario
    info_pessoa = buscar_pessoa_view.buscar_pessoa_view()

    # envia a resposta do usuario para o controller
    resposta = buscar_pessoa_controller.buscar_por_nome(info_pessoa, repositorio)

    if resposta["sucesso"]:
        buscar_pessoa_view.buscar_pessoa_sucesso(resposta)
    else:
        buscar_pessoa_view.buscar_pessoa_falha(resposta["erro"])
    
    