import unittest
from mongo_api import create_hospede, get_hospedes, delete_hospede
from pymongo import MongoClient
from dotenv import load_dotenv
import os

class TestMongoAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        mongo_uri = os.getenv('MONGO_URI')
        client = MongoClient(mongo_uri)
        cls.db = client['HOTEL']
        cls.hospede_collection = cls.db.hospedes

    def setUp(self):
        # Limpar a coleção antes de cada teste
        self.hospede_collection.delete_many({})

    def test_create_and_get_hospede(self):
        # Dados de teste
        hospede_data = {
            "nome": "Maria Souza",
            "documento_identificacao": "98765432100",
            "data_nascimento": "1992-09-21",
            "historico_reservas": [],
            "contato": {"email": "maria@example.com", "telefone": "555-4321"}
        }
        
        # Testar criação
        create_hospede(hospede_data)
        hospedes = get_hospedes()

        # Verificar se o hóspede foi inserido
        self.assertEqual(len(hospedes), 1)
        self.assertEqual(hospedes[0]['nome'], "Maria Souza")

    def test_delete_hospede(self):
        # Inserir um hóspede para testar a exclusão
        hospede_data = {
            "nome": "João Silva",
            "documento_identificacao": "12345678900",
            "data_nascimento": "1990-10-10",
            "historico_reservas": [],
            "contato": {"email": "joao@example.com", "telefone": "555-6789"}
        }
        create_hospede(hospede_data)

        # Verificar que foi criado
        hospedes = get_hospedes()
        hospede_id = hospedes[0]['_id']

        # Testar exclusão
        delete_hospede(hospede_id)
        hospedes = get_hospedes()

        # Verificar se foi deletado
        self.assertEqual(len(hospedes), 0)

# Executar os testes
if __name__ == '__main__':
    unittest.main()
