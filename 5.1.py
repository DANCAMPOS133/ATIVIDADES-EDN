# Calculando gorjetas apartir do valor da conta.

print("=== CALCULADORA DE GORJETA ===")

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)
    
try:
    conta = float(input("Digite o valor total da conta (R$): "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))

    valor_gorjeta = calcular_gorjeta(conta, porcentagem)
    total_geral = conta + valor_gorjeta

    print("\n--- RESUMO DO PAGAMENTO ---")
    print(f"Valor da Conta:   R$ {conta:>8.2f}")
    print(f"Gorjeta ({porcentagem}%): R$ {valor_gorjeta:>8.2f}")
    print("-" * 27)
    print(f"TOTAL A PAGAR:    R$ {total_geral:>8.2f}")

except ValueError:
    print("Erro: Por favor, insira apenas números válidos (use ponto em vez de vírgula).")