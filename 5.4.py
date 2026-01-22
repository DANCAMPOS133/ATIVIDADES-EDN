# Calculando o valor dos descontos 

print("=== CALCULANDO OS DESCONTOS ===")

def calcular_preco_final(preco_original, porcentagem_desconto):
    
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    
    preco_final = preco_original - valor_desconto
    
    return round(valor_desconto, 2), round(preco_final, 2)

try:
    preco = float(input("Digite o preço original do produto (R$): "))
    desconto_pct = float(input("Digite a porcentagem de desconto (%): "))

    v_desconto, p_final = calcular_preco_final(preco, desconto_pct)

    print("-" * 30)
    print(f"Preço Original:  R$ {preco:.2f}")
    print(f"Valor Descontado: R$ {v_desconto:.2f}")
    print(f"Preço Final:     R$ {p_final:.2f}")
    print("-" * 30)

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")