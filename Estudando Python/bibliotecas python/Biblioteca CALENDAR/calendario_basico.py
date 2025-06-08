# https://docs.python.org/pt-br/3.9/library/calendar.html#calendar.setfirstweekday

import calendar
# o modulo calendar trabalha com o calendario gregoriano
# o primeiro dia da semana começa com segunda-feira indice 0

ano = 2025
mes = 3 # escolher um mês aleatorio para testes

# podemos escolher o dia da semana para começar
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(ano, mes))

# podemos checar se o ano é bissexto
ano_bissexto = calendar.isleap(ano)
print(f'O ano {ano} é bissexto: {ano_bissexto}')

# podemos descobrir quantos anos bissextos temos em um interalo de tempo
total_anos_bissexto = calendar.leapdays(ano, ano + 10) # proximos 10 anos
print(f"Nos proximos 10 anos teremos {total_anos_bissexto} anos bissextos")

# podemos obter o dia da semana de uma determinada data
dia_da_semana = calendar.weekday(ano, mes, 3) # que dia cai meu aniversario

if dia_da_semana == 0:
    print('Meu aniversario cai em uma SEGUNDA-FEIRA')
elif dia_da_semana == 1:
    print('Meu aniversario cai em uma TERÇA-FEIRA')
elif dia_da_semana == 2:
    print('Meu aniversario cai em uma QUARTA-FEIRA')
elif dia_da_semana == 3:
    print('Meu aniversario cai em uma QUiNTA-FEIRA')
elif dia_da_semana == 4:
    print('Meu aniversario cai em uma SEXTA-FEIRA')
elif dia_da_semana == 5:
    print('Meu aniversario cai em um SÁBADO')
elif dia_da_semana == 6:
    print('Meu aniversario cai em um DOMINGO')

# também podemos descobrir qual vai ser o primeiro dia do mes
# e quantos dias o mês vai ter
# retorna uma tupla
primeiro_dia = calendar.monthrange(ano, mes)[0]

if primeiro_dia == 0:
    print(f'Esse mês começa em uma SEGUNDA-FEIRA')
elif primeiro_dia == 1:
    print(f'Esse mês começa em uma TERÇA-FEIRA')
elif primeiro_dia == 2:
    print(f'Esse mês começa em uma QUARTA-FEIRA')
elif primeiro_dia == 3:
    print(f'Esse mês começa em uma QUiNTA-FEIRA')
elif primeiro_dia == 4:
    print(f'Esse mês começa em uma SEXTA-FEIRA')
elif primeiro_dia == 5:
    print(f'Esse mês começa em um SÁBADO')
elif primeiro_dia == 6:
    print(f'Esse mês começa em um DOMINGO')

# pegamos o total de dias do mes
quantos_dias_tem = calendar.monthrange(ano, mes)[1]

print(f"Esse mês tem {quantos_dias_tem} dias")

# podemos obter o nome de todos os dias da semana
# precisamos passar o day_name para uma lista
dias_da_semana = list(calendar.day_name)
print(dias_da_semana)