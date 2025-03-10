import requests

# URL da API
url = 'https://www.mfcopenapi.info/open/api/playlist/videos/v1'

# Parâmetros da requisição (coloque a playlistId que você deseja)
params = {
    'playlistId': 'ID_DA_PLAYLIST',  # Substitua pelo ID da playlist que deseja acessar
    'language': 'PT',  # Ou 'EN' para inglês
    'pageId': 1,  # Primeira página (se tiver mais de uma)
    'pageSize': 10  # Número de vídeos por página
}

# Enviando a requisição GET
response = requests.get(url, params=params)

# Verificando o status da resposta
if response.status_code == 200:
    # Se a requisição foi bem-sucedida, mostra os dados em formato JSON
    data = response.json()
    print("Dados recebidos:", data)
else:
    print(f"Erro na requisição: {response.status_code}")
