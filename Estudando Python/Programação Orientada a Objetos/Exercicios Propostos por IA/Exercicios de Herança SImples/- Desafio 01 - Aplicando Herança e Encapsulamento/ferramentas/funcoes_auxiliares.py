import re

import random

def gerador_de_cpf():

    def gerar_digito_verificador(cpf_base):
        """
        Gera um dígito verificador para o CPF baseado nos 9 ou 10 primeiros dígitos.

        Args:
            cpf_base (list): Lista de inteiros com 9 ou 10 dígitos do CPF.

        Returns:
            int: Dígito verificador calculado.
        """
        peso = len(cpf_base) + 1
        soma = sum([valor * (peso - i) for i, valor in enumerate(cpf_base)])
        digito = (soma * 10) % 11
        return digito if digito < 10 else 0

    def gerar_cpf(formatado: bool = False) -> str:
        """
        Gera um CPF válido aleatório.

        Args:
            formatado (bool): Se True, retorna o CPF com pontos e traço (###.###.###-##)

        Returns:
            str: CPF gerado.
        """
        cpf = [random.randint(0, 9) for _ in range(9)]

        # Gera os dois dígitos verificadores
        cpf.append(gerar_digito_verificador(cpf))
        cpf.append(gerar_digito_verificador(cpf))

        cpf_str = ''.join(map(str, cpf))

        if formatado:
            return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
        return cpf_str
    
    return gerar_cpf(False)



def limpar_cpf(documento: str) -> str:
    """
    Remove todos os caracteres não numéricos de um CPF.

    Args:
        documento (str): String contendo o CPF com ou sem pontuação.

    Returns:
        str: CPF contendo apenas os 11 dígitos numéricos.
    """
    return re.sub(r"\D", "", documento)


def buscar_caracteres_especiais(texto: str) -> bool:
    """
    Verifica se há caracteres especiais em uma string.

    Args:
        texto (str): Texto a ser analisado.

    Returns:
        bool: True se houver ao menos um caractere especial, False caso contrário.
    """
    return bool(re.search(r"[^\w\s]", texto))


def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF com base nos critérios definidos pela Receita Federal.

    Regras de validação:
    - Deve conter exatamente 11 dígitos numéricos.
    - Não pode conter todos os dígitos iguais (ex: '11111111111').
    - Deve passar pela validação dos dígitos verificadores.

    Args:
        cpf (str): CPF contendo apenas números.

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    if len(cpf) != 11:
        print("CPF inválido: deve conter 11 dígitos.")
        return False

    if cpf == cpf[0] * 11:
        print("CPF inválido: todos os dígitos são iguais.")
        return False

    # Cálculo do primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # Verifica se os dígitos verificadores estão corretos
    if cpf[-2:] != f"{digito1}{digito2}":
        print("CPF inválido: dígitos verificadores incorretos.")
        return False

    print("CPF válido.")
    return True


def validar_senha(senha: str) -> bool:
    """
    Valida se a senha atende aos critérios de segurança.

    Regras de validação:
    - Mínimo de 8 caracteres.
    - Deve conter pelo menos uma letra.
    - Deve conter pelo menos um número.
    - Deve conter pelo menos um caractere especial.

    Args:
        senha (str): Senha a ser validada.

    Returns:
        bool: True se a senha for válida, False caso contrário.
    """
    if len(senha) < 8:
        print("Senha inválida: deve ter no mínimo 8 caracteres.")
        return False

    tem_letras = any(char.isalpha() for char in senha)
    tem_numeros = any(char.isdigit() for char in senha)
    tem_especiais = buscar_caracteres_especiais(senha)

    if not (tem_letras and tem_numeros and tem_especiais):
        print("Senha inválida: deve conter letras, números e caracteres especiais (ex: @, #, %).")
        return False

    print("Senha válida.")
    return True


def validar_nome(nome: str) -> bool:
    """
    Valida se o nome é considerado completo.

    Regras de validação:
    - Deve conter pelo menos duas palavras (ex: nome + sobrenome).
    - Deve ter ao menos dois caracteres.

    Args:
        nome (str): Nome completo da pessoa.

    Returns:
        bool: True se o nome for considerado completo, False caso contrário.
    """
    lista = nome.split()

    if len(lista) < 2 or len(nome.strip()) < 2:
        print("Nome inválido: informe o nome completo (nome e sobrenome).")
        return False

    print("Nome válido.")
    return True


def validar_salario(salario: float) -> bool:
    """
    Verifica se o salário é um valor positivo.

    Args:
        salario (float): Valor do salário a ser validado.

    Returns:
        bool: True se o salário for maior que zero, False caso contrário.
    """
    if salario <= 0:
        print("Salário inválido: o valor deve ser maior que zero.")
        return False

    print("Salário válido.")
    return True

def calcular_aumento_salarial(salario: float, porcentagem: int) -> float:
    """
    Calcula o novo salário após um aumento percentual.

    Args:
        salario (float): Salário atual do funcionário.
        porcentagem (int): Percentual de aumento (ex: 15 para 15%).

    Returns:
        float: Novo salário com o aumento aplicado.
    """

    # Converte o valor percentual para decimal (ex: 15 → 0.15)
    aumento_decimal = porcentagem / 100

    # Retorna o novo salário com o aumento aplicado
    return salario + (salario * aumento_decimal)
