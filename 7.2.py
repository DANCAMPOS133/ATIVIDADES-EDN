import csv

def criar_csv(caminho_arquivo):
    dados = [["Nome", "Idade", "Cidade"]]

    try:
        quantidade = int(input("Quantas pessoas deseja cadastrar? "))

        for i in range(quantidade):
            print(f"\nPessoa {i + 1}:")
            nome = input("Nome: ")
            idade = input("Idade: ")
            cidade = input("Cidade: ")

            dados.append([nome, idade, cidade])

        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(dados)

        print("\nArquivo CSV salvo com sucesso!")

    except Exception as e:
        print(f"\nFalha ao salvar o arquivo: {e}")

# Programa principal
caminho = input("Digite o nome ou caminho do arquivo CSV: ")
criar_csv(caminho)