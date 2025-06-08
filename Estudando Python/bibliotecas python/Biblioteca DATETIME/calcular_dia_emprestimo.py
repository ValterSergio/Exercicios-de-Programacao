from datetime import datetime
from dateutil.relativedelta import relativedelta

# criar data emprestimo
data_emprestimo = datetime(2020, 12, 20)

# obter data final do emprestimo
data_final = data_emprestimo + relativedelta(years=5)

# valor do emprestimo
valor_emprestimo = 1_000_000

# valor de cada parcela
valor_parcela = valor_emprestimo / (5 * 12)

atual = 0
while data_emprestimo < data_final:
    print("-" * 79)
    print(f'Parcela : {atual + 1}')
    vencimento = data_emprestimo + relativedelta(months=1)
    print(f"Data de vencimento: {vencimento.strftime('%d/%m/%y')}")
    print(f"Valor da parcela: {valor_parcela:,.2f}")
    print("-" * 79)
    data_emprestimo = vencimento
    atual += 1