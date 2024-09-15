import unittest
from unittest.mock import patch
from controllers.hospede_controller import HospedeController

class TestHospedeController(unittest.TestCase):

    @patch('controllers.hospede_controller.create_hospede')  # Mockando a função do mongo_api
    def test_criar_hospede_sucesso(self, mock_create_hospede):
        # Dados válidos
        dados_validos = {
            "nome": "João da Silva",
            "documento_identificacao": "12345678900",
            "data_nascimento": "1990-05-20",
            "historico_reservas": [],
            "contato": {"email": "joao@example.com", "telefone": "555-1234"}
        }
        
        # Chama o controlador
        HospedeController.criar_hospede(dados_validos)

        # Verifica se a função create_hospede foi chamada corretamente
        mock_create_hospede.assert_called_once_with(dados_validos)

    def test_criar_hospede_falha_sem_nome(self):
        # Dados inválidos: Sem nome
        dados_invalidos = {
            "documento_identificacao": "12345678900",
            "data_nascimento": "1990-05-20",
            "historico_reservas": [],
            "contato": {"email": "joao@example.com", "telefone": "555-1234"}
        }

        # Verifica se o controlador lança uma exceção quando o nome está ausente
        with self.assertRaises(ValueError) as context:
            HospedeController.criar_hospede(dados_invalidos)
        
        self.assertEqual(str(context.exception), "Nome do hóspede é obrigatório")

    def test_criar_hospede_falha_email_invalido(self):
        # Dados inválidos: Email inválido
        dados_invalidos = {
            "nome": "João da Silva",
            "documento_identificacao": "12345678900",
            "data_nascimento": "1990-05-20",
            "historico_reservas": [],
            "contato": {"email": "joaoatexample.com", "telefone": "555-1234"}  # Email inválido
        }

        # Verifica se o controlador lança uma exceção quando o email é inválido
        with self.assertRaises(ValueError) as context:
            HospedeController.criar_hospede(dados_invalidos)
        
        self.assertEqual(str(context.exception), "Email inválido")

# Executar os testes
if __name__ == '__main__':
    unittest.main()
