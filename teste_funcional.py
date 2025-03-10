import requests

# URL da API
url = "https://www.advantageonlineshopping.com/catalog/api/v1/products"

# Fazendo a requisição GET
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    print(response.json())  # Exibe a resposta em formato JSON
else:
    print(f"Erro ao acessar a API: {response.status_code}")
