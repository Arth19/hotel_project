import unittest
from unittest.mock import patch, Mock
from controllers.operacao_controller import OperacaoController

class TestOperacaoController(unittest.TestCase):

    @patch('controllers.operacao_controller.create_operacao')
    def test_criar_operacao_sucesso(self, mock_create_operacao):
        mock_create_operacao.return_value = None
        nova_operacao = {
            "reserva_id": "123",
            "tipo_operacao": "check-in",
            "data_operacao": "2024-09-15T14:00:00Z"
        }
        OperacaoController.criar_operacao(nova_operacao)
        mock_create_operacao.assert_called_once_with(nova_operacao)

    def test_criar_operacao_falha_sem_reserva_id(self):
        nova_operacao = {
            "tipo_operacao": "check-in",
            "data_operacao": "2024-09-15T14:00:00Z"
        }
        with self.assertRaises(ValueError) as context:
            OperacaoController.criar_operacao(nova_operacao)
        self.assertEqual(str(context.exception), "ID da reserva é obrigatório")

    def test_criar_operacao_falha_tipo_operacao_invalido(self):
        nova_operacao = {
            "reserva_id": "123",
            "tipo_operacao": "cancelamento",  # Tipo inválido
            "data_operacao": "2024-09-15T14:00:00Z"
        }
        with self.assertRaises(ValueError) as context:
            OperacaoController.criar_operacao(nova_operacao)
        self.assertEqual(str(context.exception), "Tipo de operação inválido")

    @patch('controllers.operacao_controller.update_operacao')
    def test_atualizar_operacao_sucesso(self, mock_update_operacao):
        novos_dados = {
            "reserva_id": "123",
            "tipo_operacao": "check-out",
            "data_operacao": "2024-09-20T11:00:00Z"
        }
        OperacaoController.atualizar_operacao("operacao_id", novos_dados)
        mock_update_operacao.assert_called_once_with("operacao_id", novos_dados)

    @patch('controllers.operacao_controller.delete_operacao')
    def test_deletar_operacao_sucesso(self, mock_delete_operacao):
        OperacaoController.deletar_operacao("operacao_id")
        mock_delete_operacao.assert_called_once_with("operacao_id")

# Executar os testes
if __name__ == '__main__':
    unittest.main()
