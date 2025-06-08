from datetime import datetime

# usamos now para a data atual
data_atual = datetime.now()

print("-" * 79)
print("PRIMEIRO EXEMPLO:\n")
print(f"Data atual: {data_atual}")
print("-" * 79)

# porem podemos pegar detalhes da data
dia = data_atual.day # pegamos o dia
mes = data_atual.month # pegamos o mês
ano = data_atual.year # pegamos o ano

print("SEGUNDO EXEMPLO:\n")
print(f"Dia: {dia} | Mês: {mes} | Ano: {ano}")
print("-" * 79)

# podemos pegar detalhes de horas 
hora = data_atual.hour # pegamos a hora
minuto = data_atual.minute # pegamos o minuto
segundo = data_atual.second # pegamos os segundos
microsegundos = data_atual.microsecond # pegamos microsegundos

print("TERCEIRO EXEMPLO:\n")
print(f"Hora: {hora} | Minuto: {minuto} | Segundo: {segundo} | Microssegundos: {microsegundos}")
print("-" * 79)