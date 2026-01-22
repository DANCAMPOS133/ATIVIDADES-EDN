import requests

def buscar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    
    try:
        I
        resposta = requests.get(url, timeout=10)
        
        resposta.raise_for_status()
        
        dados = resposta.json()
        usuario = dados['results'][0]
        
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("-" * 30)
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        print("-" * 30)

    except requests.exceptions.RequestException as e:
        
        print(f"Falha na conexão: Não foi possível acessar a API.")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    buscar_usuario_aleatorio()
