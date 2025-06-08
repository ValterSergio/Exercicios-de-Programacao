import calendar
import locale

# podemos descobrir a localidade manualmente antes de qualquer coisa
obter_local = locale.getlocale() # retorna uma str com o local e a codificação de caractere

pegar_local = obter_local[0] # retorna "pt_BR" no caso de brasil
pegar_codificacao = obter_local[1] # retorna a codificação de caracteres

print(f'Local: {pegar_local} | Codificação: {pegar_codificacao}')

# queremos mudar a localidade do programa
# podemos usar a localidade padrão do sistema
# defindo a categoria ( um tipo de locale )

# o segundo parametro vazio usa a localidade padrão do sistema
# podemos definir a codificação de caracteres com '.utf8' ou tra que necessite
locale.setlocale(locale.LC_ALL, f'{pegar_local}.utf8') 

# isso cria o dicionario em português
calendario = calendar.calendar(2025)

# exibir dicionario traduzido
print(calendario)

# por recomendação só pode alterar o locale apenas uma vez, para evitar problemas com threads