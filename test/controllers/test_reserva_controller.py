import unittest
from unittest.mock import patch, Mock
from controllers.reserva_controller import ReservaController

class TestReservaController(unittest.TestCase):

    @patch('controllers.reserva_controller.create_reserva')
    def test_criar_reserva_sucesso(self, mock_create_reserva):
        mock_create_reserva.return_value = None  # Simula sucesso
        nova_reserva = {
            "hospede_id": "123",
            "quarto_id": "456",
            "data_checkin": "2024-09-15T14:00:00Z",
            "data_checkout": "2024-09-20T11:00:00Z",
            "status": "confirmada"
        }
        ReservaController.criar_reserva(nova_reserva)
        mock_create_reserva.assert_called_once_with(nova_reserva)

    def test_criar_reserva_falha_sem_hospede_id(self):
        nova_reserva = {
            "quarto_id": "456",
            "data_checkin": "2024-09-15T14:00:00Z",
            "data_checkout": "2024-09-20T11:00:00Z",
            "status": "confirmada"
        }
        with self.assertRaises(ValueError) as context:
            ReservaController.criar_reserva(nova_reserva)
        self.assertEqual(str(context.exception), "ID do hóspede é obrigatório")

    def test_criar_reserva_falha_data_checkout_invalida(self):
        nova_reserva = {
            "hospede_id": "123",
            "quarto_id": "456",
            "data_checkin": "2024-09-20T14:00:00Z",
            "data_checkout": "2024-09-15T11:00:00Z",  # Data inválida
            "status": "confirmada"
        }
        with self.assertRaises(ValueError) as context:
            ReservaController.criar_reserva(nova_reserva)
        self.assertEqual(str(context.exception), "A data de check-out deve ser posterior à data de check-in")

    @patch('controllers.reserva_controller.update_reserva')
    def test_atualizar_reserva_sucesso(self, mock_update_reserva):
        novos_dados = {
            "hospede_id": "123",
            "quarto_id": "456",
            "data_checkin": "2024-09-15T14:00:00Z",
            "data_checkout": "2024-09-20T11:00:00Z",
            "status": "confirmada"
        }
        ReservaController.atualizar_reserva("reserva_id", novos_dados)
        mock_update_reserva.assert_called_once_with("reserva_id", novos_dados)

    @patch('controllers.reserva_controller.delete_reserva')
    def test_deletar_reserva_sucesso(self, mock_delete_reserva):
        ReservaController.deletar_reserva("reserva_id")
        mock_delete_reserva.assert_called_once_with("reserva_id")

# Executar os testes
if __name__ == '__main__':
    unittest.main()
