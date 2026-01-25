import csv

def ler_csv(caminho_arquivo):
    try:
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Programa principal
caminho = input("Digite o nome ou caminho do arquivo CSV: ")
ler_csv(caminho)


