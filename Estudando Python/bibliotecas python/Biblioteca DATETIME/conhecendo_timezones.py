from datetime import datetime
import pytz

# Podemos definir um fuso horario
fuso_sp = pytz.timezone("America/Sao_Paulo")
data_sp = datetime.now(fuso_sp)

print("-" * 79)
print("PRIMEIRO EXEMPLO\n")
print(f"Hora em São Paulo: {data_sp.strftime("%H:%M:%S")}")


# Que horas é em londres?
fuso_londres = pytz.timezone("Europe/London") # definindo o fuso para londres
data_londres = datetime.now(fuso_londres)
print("-" * 79)
print("SEGUNDO EXEMPLO\n")
print(f"Hora em Londres: {data_londres.strftime("%H:%M:%S")}")

# podemos obter uma lista de todos os fuso horarios disponiveis
fusos_do_mundo = pytz.all_timezones

print("-" * 79)
print("TERCEIRO EXEMPLO\n")
print("--- FUSOS HORARIOS DISPONIVEIS ---")
for fuso in fusos_do_mundo:
    print(f'Fuso: {fuso}')
print()
print(f'Temos uma lista de {len(fusos_do_mundo)} fusos horarios disponiveis')
print("-" * 79)