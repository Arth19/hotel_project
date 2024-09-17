import unittest
from unittest.mock import patch, Mock
import astra_api

class TestAstraAPI(unittest.TestCase):

    # Testes para CRUD de Reservas
    @patch('astra_api.requests.post')
    def test_create_reserva_sucesso(self, mock_post):
        # Simular uma resposta de sucesso da API
        mock_post.return_value = Mock(status_code=201)
        
        # Dados de teste
        reserva_data = {
            "reserva_id": "12345",
            "hospede_id": "67890",
            "quarto_id": "54321",
            "data_checkin": "2024-09-15T14:00:00Z",
            "data_checkout": "2024-09-20T11:00:00Z",
            "status": "confirmada"
        }

        # Chamar a função
        astra_api.create_reserva(reserva_data)
        
        # Verificar se a função POST foi chamada corretamente
        mock_post.assert_called_once_with(
            f"{astra_api.BASE_URL}reservas",
            headers=astra_api.HEADERS,
            json=reserva_data
        )

    @patch('astra_api.requests.get')
    def test_get_reservas_sucesso(self, mock_get):
        # Simular uma resposta de sucesso com reservas
        mock_get.return_value = Mock(status_code=200, json=lambda: {"data": [{"reserva_id": "12345"}]})
        
        # Chamar a função
        reservas = astra_api.get_reservas()
        
        # Verificar se a função GET foi chamada corretamente
        mock_get.assert_called_once_with(
            f"{astra_api.BASE_URL}/reservas",
            headers=astra_api.HEADERS,
            params={'where': '{}'}
        )
        
        # Verificar se o resultado está correto
        self.assertEqual(reservas, [{"reserva_id": "12345"}])

    @patch('astra_api.requests.put')
    def test_update_reserva_sucesso(self, mock_put):
        # Simular uma resposta de sucesso ao atualizar uma reserva
        mock_put.return_value = Mock(status_code=200)
        
        # Dados de teste
        novos_dados = {
            "status": "cancelada"
        }
        
        # Chamar a função
        astra_api.update_reserva("12345", novos_dados)
        
        # Verificar se a função PUT foi chamada corretamente
        mock_put.assert_called_once_with(
            f"{astra_api.BASE_URL}reservas/12345",
            headers=astra_api.HEADERS,
            json=novos_dados
        )

    @patch('astra_api.requests.delete')
    def test_delete_reserva_sucesso(self, mock_delete):
        # Simular uma resposta de sucesso ao deletar uma reserva
        mock_delete.return_value = Mock(status_code=204)
        
        # Chamar a função
        astra_api.delete_reserva("12345")
        
        # Verificar se a função DELETE foi chamada corretamente
        mock_delete.assert_called_once_with(
            f"{astra_api.BASE_URL}reservas/12345",
            headers=astra_api.HEADERS
        )

    # Testes para CRUD de Faturamento
    @patch('astra_api.requests.post')
    def test_create_faturamento_sucesso(self, mock_post):
        mock_post.return_value = Mock(status_code=201)
        faturamento_data = {
            "faturamento_id": "54321",
            "reserva_id": "12345",
            "valor_total": 1500.00,
            "metodo_pagamento": "cartao"
        }
        astra_api.create_faturamento(faturamento_data)
        mock_post.assert_called_once_with(
            f"{astra_api.BASE_URL}faturamento",
            headers=astra_api.HEADERS,
            json=faturamento_data
        )

    @patch('astra_api.requests.get')
    def test_get_faturamentos_sucesso(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {"data": [{"faturamento_id": "54321"}]})
        faturamentos = astra_api.get_faturamentos()
        mock_get.assert_called_once_with(
            f"{astra_api.BASE_URL}faturamento",
            headers=astra_api.HEADERS
        )
        self.assertEqual(faturamentos, [{"faturamento_id": "54321"}])

    @patch('astra_api.requests.put')
    def test_update_faturamento_sucesso(self, mock_put):
        mock_put.return_value = Mock(status_code=200)
        novos_dados = {
            "valor_total": 1600.00
        }
        astra_api.update_faturamento("54321", novos_dados)
        mock_put.assert_called_once_with(
            f"{astra_api.BASE_URL}faturamento/54321",
            headers=astra_api.HEADERS,
            json=novos_dados
        )

    @patch('astra_api.requests.delete')
    def test_delete_faturamento_sucesso(self, mock_delete):
        mock_delete.return_value = Mock(status_code=204)
        astra_api.delete_faturamento("54321")
        mock_delete.assert_called_once_with(
            f"{astra_api.BASE_URL}faturamento/54321",
            headers=astra_api.HEADERS
        )

    # Testes para CRUD de Operações
    @patch('astra_api.requests.post')
    def test_create_operacao_sucesso(self, mock_post):
        mock_post.return_value = Mock(status_code=201)
        operacao_data = {
            "operacao_id": "67890",
            "reserva_id": "12345",
            "tipo_operacao": "check-in",
            "data_operacao": "2024-09-15T14:00:00Z"
        }
        astra_api.create_operacao(operacao_data)
        mock_post.assert_called_once_with(
            f"{astra_api.BASE_URL}operacoes",
            headers=astra_api.HEADERS,
            json=operacao_data
        )

    @patch('astra_api.requests.get')
    def test_get_operacoes_sucesso(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {"data": [{"operacao_id": "67890"}]})
        operacoes = astra_api.get_operacoes()
        mock_get.assert_called_once_with(
            f"{astra_api.BASE_URL}operacoes",
            headers=astra_api.HEADERS
        )
        self.assertEqual(operacoes, [{"operacao_id": "67890"}])

    @patch('astra_api.requests.put')
    def test_update_operacao_sucesso(self, mock_put):
        mock_put.return_value = Mock(status_code=200)
        novos_dados = {
            "tipo_operacao": "check-out"
        }
        astra_api.update_operacao("67890", novos_dados)
        mock_put.assert_called_once_with(
            f"{astra_api.BASE_URL}operacoes/67890",
            headers=astra_api.HEADERS,
            json=novos_dados
        )

    @patch('astra_api.requests.delete')
    def test_delete_operacao_sucesso(self, mock_delete):
        mock_delete.return_value = Mock(status_code=204)
        astra_api.delete_operacao("67890")
        mock_delete.assert_called_once_with(
            f"{astra_api.BASE_URL}operacoes/67890",
            headers=astra_api.HEADERS
        )


# Executar os testes
if __name__ == '__main__':
    unittest.main()
