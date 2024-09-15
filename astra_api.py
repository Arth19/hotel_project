import os
import requests
from dotenv import load_dotenv

# Carregar as variáveis de ambiente
load_dotenv()

# Obter as variáveis do ambiente
ASTRA_DB_ID = os.getenv('ASTRA_DB_ID')
ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_REGION = os.getenv('ASTRA_DB_REGION')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')

# Base URL da API REST do Astra
BASE_URL = f'https://{ASTRA_DB_ID}-{ASTRA_DB_REGION}.apps.astra.datastax.com/api/rest/v2/keyspaces/{ASTRA_DB_KEYSPACE}'

# Cabeçalhos para autenticação
headers = {
    'X-Cassandra-Token': ASTRA_DB_APPLICATION_TOKEN,
    'Content-Type': 'application/json'
}

# Função de exemplo para buscar dados da tabela reservas filtrando por um UUID específico
def get_reservas():
    url = f'{BASE_URL}/reservas'
    params = {
        'where': '{"reserva_id": {"$eq": "550e8400-e29b-41d4-a716-446655440000"}}'  # Substitua por um UUID válido
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar reservas: {response.status_code} - {response.text}")

# Testando a conexão e buscando reservas
reservas = get_reservas()
if reservas:
    print("Reservas encontradas:")
    print(reservas)
