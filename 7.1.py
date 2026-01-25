import pandas as pd

def analisar_logs_treinamento(caminho_arquivo):
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_arquivo)

        # Verifica se a coluna existe
        if "tempo_execucao" not in df.columns:
            print("❌ Erro: a coluna 'tempo_execucao' não foi encontrada no arquivo.")
            return

        # Calcula média e desvio padrão
        media = df["tempo_execucao"].mean()
        desvio_padrao = df["tempo_execucao"].std()

        print("📈 Estatísticas do tempo de execução:")
        print(f"Média         : {media:.2f}")
        print(f"Desvio padrão : {desvio_padrao:.2f}")

    except FileNotFoundError:
        print("❌ Erro: arquivo não encontrado.")
    except pd.errors.EmptyDataError:
        print("❌ Erro: o arquivo CSV está vazio.")
    except pd.errors.ParserError:
        print("❌ Erro: falha ao interpretar o arquivo CSV.")
    except Exception as erro:
        print(f"❌ Erro inesperado: {erro}")


# Programa principal
arquivo = input("Digite o caminho do arquivo CSV de logs de treinamento: ")
analisar_logs_treinamento(arquivo)

