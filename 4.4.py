# Analisador de Números: Pares ou ímpares

print("=== ANALISADOR DE NUMEROS PARES OU IMPARES ===")

qtd = int(input("Quantos números você quer analisar? "))
pares = 0
impares = 0

for i in range(qtd):
    n = int(input(f"Digite o {i+1}º número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nAnálise concluída:")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
