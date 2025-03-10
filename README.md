# Projeto: Integração com a MFC Meta API

Este projeto tem como objetivo integrar e utilizar a **MFC Meta API** para buscar informações de vídeos e playlists. A API oferece dados sobre vídeos, como título, descrição, imagem, avaliação, e outros metadados.

## Descrição

O código permite que você faça requisições para a MFC Meta API usando o Python e a biblioteca `requests`, para obter dados de playlists e vídeos. O projeto também inclui instruções para configurar o ambiente, instalar pacotes necessários e testar a integração com a API.

## Funcionalidades

- **Consulta a Playlists e Vídeos**: Você pode buscar informações sobre playlists e vídeos específicos através de parâmetros como `playlistId`, `language`, `pageId`, e `pageSize`.
- **Exibição dos Dados**: O projeto exibe os dados recebidos da API de forma organizada, como título, descrição, gênero e outros metadados de vídeos.
- **Uso de Parâmetros Dinâmicos**: O código permite que você personalize suas requisições, como escolher a linguagem da resposta ou a quantidade de vídeos por página.

## Tecnologias Utilizadas

- **Python 3.x**: A linguagem utilizada para fazer requisições à API e manipulação dos dados.
- **requests**: Biblioteca Python para enviar requisições HTTP à API e processar as respostas.
- **JSON**: O formato de dados utilizado pela API, processado e exibido no código.

## Como Rodar o Projeto

### 1. Requisitos

- Python 3.x instalado.
- `pip` (gerenciador de pacotes do Python).
  
### 2. Instalar Dependências

Antes de executar o código, é necessário instalar as dependências. No terminal, execute o seguinte comando:

```bash
pip install requests
