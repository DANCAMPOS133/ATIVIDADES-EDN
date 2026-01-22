mport requests
from datetime import datetime

def consultar_moeda(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("❌ Moeda não encontrada.")
            return

        info = dados[chave]

        valor_atual = info["bid"]
        maxima = info["high"]
        minima = info["low"]
        timestamp = int(info["timestamp"])
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        print("💱 Cotação da moeda:")
        print(f"Moeda            : {moeda} → BRL")
        print(f"Valor atual      : R$ {valor_atual}")
        print(f"Máxima do dia    : R$ {maxima}")
        print(f"Mínima do dia    : R$ {minima}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.RequestException:
        print("❌ Erro na requisição. Verifique sua conexão.")
    except (KeyError, ValueError):
        print("❌ Erro ao processar os dados da API.")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_moeda(moeda)