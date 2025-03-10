import requests

# URL para registro de um novo usuário
register_url = "https://www.advantageonlineshopping.com/accountservice/accountrest/api/v1/register"

# Dados para criar um novo usuário
user_data = {
    "accountType": "ADMIN", # ADMIN conforme solicitado
    "address": "#", #Insira um endereço
    "allowOffersPromotion": True,
    "aobUser": True,
    "cityName": "São Paulo",
    "country": "BRAZIL_BR",
    "email": "#", #Insira um email válido
    "firstName": "#", #Insira um primeiro nome
    "lastName": "#", #Insira um sobrenome
    "loginName": "#", #Insira um nome de login
    "password": "#", #Insira uma senha
    "phoneNumber": "#", #Insira um número de telefone
    "stateProvince": "SP",
    "zipcode": "#" #Insira um CEP
}

# Registrando o novo usuário
register_response = requests.post(register_url, json=user_data)

if register_response.status_code == 200:
    print("Usuário criado com sucesso!")
else:
    print("Erro ao criar usuário:", register_response.status_code, register_response.text)
    exit()

# URL de login do novo usuário
login_url = "https://www.advantageonlineshopping.com/accountservice/accountrest/api/v1/login"

# Dados para login (pegues da criação de usuario)
login_data = {
    "email": user_data["email"],
    "loginPassword": user_data["password"],
    "loginUser": user_data["loginName"]
}

# Headers para a requisição (adicionando Content-Type)
headers = {
    "Content-Type": "application/json", # Certifique-se de que é enviado como JSON
    "Accept": "application/json" # Aceitar resposta em JSON
}

# Realizando o login do novo usuário
login_response = requests.post(login_url, json=login_data, headers=headers)

# Verificando o status da resposta
if login_response.status_code == 200:
    print("Login do novo usuário bem-sucedido!")
    login_json = login_response.json()
    user_id = login_json['statusMessage']['userId'] # Pega o userId da resposta
    token = login_json['statusMessage']['token'] # Pega o token da resposta
    print("Resposta completa:", login_json)
else:
    print("Erro no login do novo usuário:", login_response.status_code)
    print("Resposta completa:", login_response.text)
    exit()

# Passo 2: Buscar um Produto
search_url = "https://www.advantageonlineshopping.com/catalog/api/v1/products/search"
search_params = {
    "name": "HP CHROMEBOOK 14 G1(ES)" # Nome do produto que você deseja buscar
}

# Realizando a busca
search_response = requests.get(search_url, params=search_params)

if search_response.status_code == 200:
    search_json = search_response.json() # Captura a resposta JSON
    print("Resposta da busca de produto:", search_json)  # Imprime o JSON completo da busca
    
    # Acessando a lista de produtos dentro de 'products'
    products_data = search_json[0]['products']
    
    print(f"Produtos encontrados: {len(products_data)}")
    for product in products_data:
        print(f"Nome: {product.get('productName', 'N/A')}, ID: {product.get('productId', 'N/A')}")
    
    if products_data:
        product_id = products_data[0]['productId']  # Pega o ID do primeiro produto encontrado
        print(f"ID do primeiro produto: {product_id}")
    else:
        print("Nenhum produto encontrado na lista.")
else:
    print("Erro na busca:", search_response.status_code, search_response.text)
    exit()

# Passo 3: Atualizar a Imagem de um Produto
image_url = f"https://www.advantageonlineshopping.com/catalog/api/v1/product/image/{user_id}/color/black"

# Imagem
image_path = 'imagem.jpg'
image_file = {'file': open(image_path, 'rb')}  # Abrindo o arquivo para envio

# Headers com o token de autenticação
headers = {
    'Authorization': f'Bearer {token}' # Usando o token recebido durante o login
}

# Dados do POST com os parâmetros necessários
data = {
    'color': 'black',
    'product_id': product_id,
    'source': 'color',
    'userId': user_id
}

# Enviando o arquivo e os dados do POST
response = requests.post(image_url, headers=headers, data=data, files=image_file)

if response.status_code == 200:
    print("Imagem do produto atualizada com sucesso!")
    print("Resposta da API:", response.json())
else:
    print("Erro ao atualizar a imagem:", response.status_code, response.text)