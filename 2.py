import requests

url_base = "youtube.com"  # URL base sem o prefixo 'www.'

def fetch_data(request_url):
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            print("Status code 200")
            print(full_url)
            # try: 
            #     # Tenta decodificar a resposta como JSON
            #     return response.json()  
            # except ValueError:
            #     # Se a resposta não for JSON, retorna o texto da resposta
            #     print(f"A resposta não é JSON: {response.text}")
            #     return None
        else:
            print(f'Erro: {(full_url)}')
            # print(f'Erro: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro: {(full_url)}')
        # print(f'Ocorreu um erro: {e}')
        return None

with open("texto2.txt", "r") as arquivo:
    for i, linha in enumerate(arquivo):
        if i < 20:
            linha = linha.strip()
            print(linha)
            # Formata a URL completa com o prefixo 'https://' e o sufixo base URL
            full_url = f"https://{linha}.{url_base}"  
            data = fetch_data(full_url)
            if data:
                print(data)
        else:
            break


