from mysql.connector import connect, Error

def obter_dados_tabela(usuario: str='seu_usuario', senha: str='sua_senha', banco_de_dados: str='seu_banco_de_dados', tabela: str='tabela_de_consulta') -> list:
    try:
        with connect(
            host='localhost',
            user=usuario,
            password=senha,
            database=banco_de_dados
        ) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {tabela};")
                return cursor.fetchall()
    except Error as e:
        print(f"Erro: {e}")
        return []

if __name__ == "__main__":
    dados =  obter_dados_tabela('seu_usuario', 'sua_senha', 'seu_banco_de_dados', 'tabela_de_consulta')
    print(dados)

