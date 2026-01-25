import json

def salvar_json(caminho_arquivo, dados):
    try:
        with open(caminho_arquivo, mode="w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso no arquivo JSON!")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        print("\nDados lidos do arquivo JSON:")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

    except FileNotFoundError:
        print("Falha ao ler o arquivo: arquivo não encontrado.")
    except Exception as e:
        print(f"Falha ao ler o arquivo: {e}")

# Programa principal
arquivo = input("Digite o nome ou caminho do arquivo JSON: ")

pessoa = {
    "nome": input("Nome: "),
    "idade": input("Idade: "),
    "cidade": input("Cidade: ")
}

salvar_json(arquivo, pessoa)
ler_json(arquivo)
