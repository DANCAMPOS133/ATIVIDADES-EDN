# Verificando se o texto é Palíndromo
print("=== ANALISADOR DE PALÍNDROMOS ===")

import unicodedata

def limpar_texto(texto):
    texto = texto.lower().replace(" ", "")
    texto = "".join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return "".join(filter(str.isalnum, texto))

def verificar_dinamico():
    
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Digite uma palavra ou frase: ")
        
        if entrada.lower() == 'sair':
            print("Encerrando !")
            break
            
        processado = limpar_texto(entrada)
        invertido = processado[::-1]
        
        if processado == invertido and processado != "":
            print(f"✅ É um palíndromo!")
    
        else:
            print(f"❌ Não é um palíndromo.")
        
        print("-" * 30)

if __name__ == "__main__":
    verificar_dinamico()