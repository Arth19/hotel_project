import unittest
from unittest.mock import patch, Mock
from controllers.faturamento_controller import FaturamentoController

class TestFaturamentoController(unittest.TestCase):

    @patch('controllers.faturamento_controller.create_faturamento')
    def test_criar_faturamento_sucesso(self, mock_create_faturamento):
        mock_create_faturamento.return_value = None
        novo_faturamento = {
            "reserva_id": "123",
            "valor_total": 500.00,
            "metodo_pagamento": "cartao"
        }
        FaturamentoController.criar_faturamento(novo_faturamento)
        mock_create_faturamento.assert_called_once_with(novo_faturamento)

    def test_criar_faturamento_falha_valor_negativo(self):
        novo_faturamento = {
            "reserva_id": "123",
            "valor_total": -500.00,  # Valor inválido
            "metodo_pagamento": "cartao"
        }
        with self.assertRaises(ValueError) as context:
            FaturamentoController.criar_faturamento(novo_faturamento)
        self.assertEqual(str(context.exception), "Valor total deve ser um valor positivo")

    def test_criar_faturamento_falha_metodo_pagamento_invalido(self):
        novo_faturamento = {
            "reserva_id": "123",
            "valor_total": 500.00,
            "metodo_pagamento": "bitcoin"  # Método inválido
        }
        with self.assertRaises(ValueError) as context:
            FaturamentoController.criar_faturamento(novo_faturamento)
        self.assertEqual(str(context.exception), "Método de pagamento inválido")

    @patch('controllers.faturamento_controller.update_faturamento')
    def test_atualizar_faturamento_sucesso(self, mock_update_faturamento):
        novos_dados = {
            "reserva_id": "123",
            "valor_total": 600.00,
            "metodo_pagamento": "dinheiro"
        }
        FaturamentoController.atualizar_faturamento("faturamento_id", novos_dados)
        mock_update_faturamento.assert_called_once_with("faturamento_id", novos_dados)

    @patch('controllers.faturamento_controller.delete_faturamento')
    def test_deletar_faturamento_sucesso(self, mock_delete_faturamento):
        FaturamentoController.deletar_faturamento("faturamento_id")
        mock_delete_faturamento.assert_called_once_with("faturamento_id")

# Executar os testes
if __name__ == '__main__':
    unittest.main()
