from src.views.registrar_pessoa_view import RegistrarPessoaView
from src.controller.registrar_pessoa_controller import RegistrarPessoaController
from src.models.repositorio.repositorio_pessoa import RepositorioPessoas

def registrar_pessoa_construtor(repositorio: RepositorioPessoas):
    registrar_pessoa = RegistrarPessoaView()
    registro_controller = RegistrarPessoaController()

    registro_info = registrar_pessoa.registrar_pessoa_view()

    # parte do controller
    resposta = registro_controller.registrar(registro_info, repositorio)

    if resposta["sucesso"]:
        registrar_pessoa.registro_de_pessoa_sucesso(resposta)
    else:
        registrar_pessoa.registro_pessoa_falha(resposta["erro"])
