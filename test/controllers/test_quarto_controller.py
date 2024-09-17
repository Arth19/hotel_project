import unittest
from unittest.mock import patch
from controllers.quarto_controller import QuartoController

class TestQuartoController(unittest.TestCase):

    @patch('controllers.quarto_controller.create_quarto')
    def test_criar_quarto_sucesso(self, mock_create_quarto):
        # Dados válidos
        dados_validos = {
            "numero_quarto": 101,
            "tipo": "suíte",
            "status": "disponível",
            "preco_diaria": 450.00,
            "caracteristicas": ["ar condicionado", "TV", "vista para o mar"]
        }
        
        # Chama o controlador
        QuartoController.criar_quarto(dados_validos)

        # Verifica se a função create_quarto foi chamada corretamente
        mock_create_quarto.assert_called_once_with(dados_validos)

    def test_criar_quarto_falha_sem_numero(self):
        # Dados inválidos: Sem número do quarto
        dados_invalidos = {
            "tipo": "suíte",
            "status": "disponível",
            "preco_diaria": 450.00,
            "caracteristicas": ["ar condicionado", "TV", "vista para o mar"]
        }

        # Verifica se o controlador lança uma exceção quando o número do quarto está ausente
        with self.assertRaises(ValueError) as context:
            QuartoController.criar_quarto(dados_invalidos)
        
        self.assertEqual(str(context.exception), "Número do quarto é obrigatório")

    def test_criar_quarto_falha_preco_invalido(self):
        # Dados inválidos: Preço da diária inválido
        dados_invalidos = {
            "numero_quarto": 101,
            "tipo": "suíte",
            "status": "disponível",
            "preco_diaria": -100.00,  # Preço inválido
            "caracteristicas": ["ar condicionado", "TV", "vista para o mar"]
        }

        # Verifica se o controlador lança uma exceção quando o preço é inválido
        with self.assertRaises(ValueError) as context:
            QuartoController.criar_quarto(dados_invalidos)
        
        self.assertEqual(str(context.exception), "Preço da diária deve ser um valor positivo")

# Executar os testes
if __name__ == '__main__':
    unittest.main()
