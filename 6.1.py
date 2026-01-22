# Gerando senhas seguras.

print("=== Gerador de Senhas Aleatórias ===")

import secrets
import string

def gerar_senha(tamanho):
    
    letras = string.ascii_letters  
    numeros = string.digits        
    simbolos = string.punctuation  
    
    todos_caracteres = letras + numeros + simbolos
    
    senha = ''.join(secrets.choice(todos_caracteres) for _ in range(tamanho))
    
    return senha

try:
    comprimento = int(input("Digite o tamanho da senha desejada (ex: 12): "))
    
    if comprimento < 4:
        print("Aviso: Senhas curtas são menos seguras. Recomendamos pelo menos 12 caracteres.")
    
    nova_senha = gerar_senha(comprimento)
    
    print("\n" + "="*20)
    print(f"Sua senha gerada é: {nova_senha}")
    print("="*20)

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros para o tamanho.")
