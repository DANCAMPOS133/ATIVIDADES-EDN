# Verificador de Senha

print(" === CRIE SUA SENHA ===")
senha = input("Digite 8 caracteres e pelo menos um numero: ")

tem_oito_caracteres = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_oito_caracteres and tem_numero:
    print("Senha segura! Atende aos critérios.")
else:
    print("Senha fraca:")
    if not tem_oito_caracteres:
        print("- Deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("- Deve conter pelo menos um número.")