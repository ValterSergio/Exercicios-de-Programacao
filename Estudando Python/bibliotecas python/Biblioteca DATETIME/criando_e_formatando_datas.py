from datetime import datetime

# criando datas ficticias
# ano mes dia - hora - minutos - segundos se quiser microssegundo(não passado)
data_false = datetime(2025, 3, 1, 16, 36, 27)

# podemos formatar essa data com strftime
dia_false_str = data_false.strftime("%d/%m/%Y") # dia - mes - ano
hora_false_str = data_false.strftime("%H:%M:%S") # hora - minuto - segundos

print("-" * 79)
print("PRIMEIRO EXEMPLO:\n")
print(f"Data criada: {dia_false_str} | Hora criada: {hora_false_str}")
print("-" * 79)
print("SEGUNDO EXEMPLO:\n")

# podemos converter uma string de data e hora em um objeto datetime com strptime
data_string = '25/12/2025 15:51:15.515151' # adicionei microssegundos 
formato_data = "%d/%m/%Y %H:%M:%S.%f"
objeto_data = datetime.strptime(data_string, formato_data)
print(f'Objeto criado(tipo): {type(objeto_data)} | Data/hora: {objeto_data}')