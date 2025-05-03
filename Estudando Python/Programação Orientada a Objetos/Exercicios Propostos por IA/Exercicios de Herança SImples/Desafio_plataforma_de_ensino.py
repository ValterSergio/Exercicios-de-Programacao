"""
Contexto do Sistema
Você está construindo um sistema para uma plataforma de cursos online. Essa plataforma lida com alunos, instrutores, cursos, aulas, avaliações e notas.
"""

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def get_cpf(self) -> str:
        return self._cpf

    def set_cpf(self, cpf: str) -> None:
        self._cpf = cpf

    def exibir_dados(self) -> None:
        print(f"Nome: {self._nome} | CPF: {self._cpf}")


class Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
        self._cursos = []

    def matricular(self, curso: str) -> None:
        self._cursos.append(curso)

    def exibir_dados(self) -> None:
        super().exibir_dados()
        print("Cursos Matriculados:")
        for curso in self._cursos:
            print(f"- {curso}")


class Instrutor(Pessoa):
    def __init__(self, nome: str, cpf: str, especialidade: str):
        super().__init__(nome, cpf)
        self._especialidade = especialidade

    def get_especialidade(self) -> str:
        return self._especialidade

    def set_especialidade(self, especialidade: str) -> None:
        self._especialidade = especialidade

    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f"Especialidade: {self._especialidade}")


class CertificadoInternacional:
    def __init__(self, instituicao: str, pais: str):
        self._instituicao = instituicao
        self._pais = pais

    def exibir_certificado(self) -> None:
        print("Certificação Internacional")
        print(f"Instituição: {self._instituicao}")
        print(f"País: {self._pais}")
        print("Parabéns pelo título de Mestre!")


class InstrutorEspecialista(Instrutor, CertificadoInternacional):
    def __init__(self, nome: str, cpf: str, especialidade: str, instituicao: str, pais: str):
        Instrutor.__init__(self, nome, cpf, especialidade)
        CertificadoInternacional.__init__(self, instituicao, pais)

    def exibir_dados(self) -> None:
        super().exibir_dados()
        self.exibir_certificado()


class Curso:
    def __init__(self, titulo: str, descricao: str):
        self._titulo = titulo
        self._descricao = descricao

    def get_titulo(self) -> str:
        return self._titulo

    def get_descricao(self) -> str:
        return self._descricao


class Aula:
    def __init__(self, titulo: str, conteudo: str):
        self._titulo = titulo
        self._conteudo = conteudo

    def exibir(self) -> None:
        print(f"Aula: {self._titulo} - Conteúdo: {self._conteudo}")


class Turma:
    def __init__(self, curso: Curso, instrutor: InstrutorEspecialista):
        self._curso = curso
        self._instrutor = instrutor
        self._alunos = []
        self._aulas = []

    def adicionar_aula(self, titulo: str, conteudo: str) -> None:
        self._aulas.append(Aula(titulo, conteudo))

    def adicionar_aluno(self, nome: str, cpf: str) -> None:
        aluno = Aluno(nome, cpf)
        aluno.matricular(self._curso.get_titulo())
        self._alunos.append(aluno)

    def exibir_instrutor(self) -> None:
        print("\n--- Instrutor da Turma ---")
        self._instrutor.exibir_dados()

    def exibir_aulas(self) -> None:
        print(f"\n--- Aulas do Curso: {self._curso.get_titulo()} ---")
        for aula in self._aulas:
            aula.exibir()

    def exibir_alunos(self) -> None:
        print("\n--- Alunos da Turma ---")
        for aluno in self._alunos:
            aluno.exibir_dados()


if __name__ == "__main__":
    instrutor = InstrutorEspecialista("João", "123", "Matemática", "UEM", "Brasil")
    curso = Curso("POO", "Paradigma de Programação Orientada a Objetos")
    turma = Turma(curso, instrutor)

    turma.adicionar_aluno("Pedro", "111")
    turma.adicionar_aluno("Paulo", "222")
    turma.adicionar_aluno("Alex", "333")

    turma.adicionar_aula("Linguagem de Programação", "Java")
    turma.adicionar_aula("Matemática", "Matemática Discreta")
    turma.adicionar_aula("Estrutura de Dados", "Notação Big O")

    turma.exibir_instrutor()
    turma.exibir_aulas()
    turma.exibir_alunos()
