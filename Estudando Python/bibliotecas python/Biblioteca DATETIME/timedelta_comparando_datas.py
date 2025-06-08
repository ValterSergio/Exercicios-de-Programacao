from datetime import datetime, timedelta

# definindo a data do natal
data_natal = datetime(2025, 12, 25)
data_natal_str = data_natal.strftime("%d/%m/%Y")

# obtendo data atual
data_atual = datetime.now()
data_atual_str = data_atual.strftime("%d/%m/%Y")

# diferença de uma data para outra
delta = data_natal - data_atual

# diferença em dias
dias_falta = delta.days

# diferença em horas
horas_falta = delta.total_seconds() // 3600

# diferença em minutos
minutos_falta = delta.total_seconds() // 60

# diferença em segundos
segundos_falta = delta.total_seconds()

# podemos somar datas
somar_data =  timedelta(days=10, hours=10) # somar 10 dias e 10 horas apartir da data de hoje
print(data_atual + somar_data)

# podemos subtrair datas
subtrair_datas = timedelta(weeks=10) # 10 semanas atras
print(data_atual - subtrair_datas)