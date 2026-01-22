# Calculando os dias vivos

print("=== QUER SABER QUANTOS DIAS ESTÁ VIVO ? ===")

from datetime import date

def dias_vivo(data_nascimento: date) -> int:
    hoje = date.today()
    return (hoje - data_nascimento).days

ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

data_nascimento = date(ano, mes, dia)

total_dias = dias_vivo(data_nascimento)

print(f"Você está vivo há {total_dias} dias.")