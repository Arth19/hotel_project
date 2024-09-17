import unittest
from unittest.mock import patch
from controllers.funcionario_controller import FuncionarioController

class TestFuncionarioController(unittest.TestCase):

    @patch('controllers.funcionario_controller.create_funcionario')
    def test_criar_funcionario_sucesso(self, mock_create_funcionario):
        # Dados válidos
        dados_validos = {
            "nome": "Maria Souza",
            "cargo": "Recepcionista",
            "data_contratacao": "2022-01-15",
            "salario": 3000,
            "turno": "diurno",
            "contato": {"email": "maria@example.com", "telefone": "555-5678"}
        }
        
        # Chama o controlador
        FuncionarioController.criar_funcionario(dados_validos)

        # Verifica se a função create_funcionario foi chamada corretamente
        mock_create_funcionario.assert_called_once_with(dados_validos)

    def test_criar_funcionario_falha_sem_nome(self):
        # Dados inválidos: Sem nome
        dados_invalidos = {
            "cargo": "Recepcionista",
            "data_contratacao": "2022-01-15",
            "salario": 3000,
            "turno": "diurno",
            "contato": {"email": "maria@example.com", "telefone": "555-5678"}
        }

        # Verifica se o controlador lança uma exceção quando o nome está ausente
        with self.assertRaises(ValueError) as context:
            FuncionarioController.criar_funcionario(dados_invalidos)
        
        self.assertEqual(str(context.exception), "Nome do funcionário é obrigatório")

    def test_criar_funcionario_falha_salario_invalido(self):
        # Dados inválidos: Salário inválido
        dados_invalidos = {
            "nome": "Maria Souza",
            "cargo": "Recepcionista",
            "data_contratacao": "2022-01-15",
            "salario": -100,  # Salário inválido
            "turno": "diurno",
            "contato": {"email": "maria@example.com", "telefone": "555-5678"}
        }

        # Verifica se o controlador lança uma exceção quando o salário é inválido
        with self.assertRaises(ValueError) as context:
            FuncionarioController.criar_funcionario(dados_invalidos)
        
        self.assertEqual(str(context.exception), "Salário deve ser um valor positivo")

# Executar os testes
if __name__ == '__main__':
    unittest.main()
