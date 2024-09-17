from astra_api import create_operacao, get_operacoes, update_operacao, delete_operacao
from datetime import datetime

class OperacaoController:

    @staticmethod
    def validar_operacao(dados):
        if "reserva_id" not in dados or not dados["reserva_id"]:
            raise ValueError("ID da reserva é obrigatório")
        
        if "tipo_operacao" not in dados or dados["tipo_operacao"] not in ["check-in", "check-out"]:
            raise ValueError("Tipo de operação inválido")
        
        if "data_operacao" not in dados or not dados["data_operacao"]:
            raise ValueError("Data da operação é obrigatória")
        
        try:
            datetime.fromisoformat(dados["data_operacao"])
        except ValueError:
            raise ValueError("Data da operação inválida")

    @staticmethod
    def criar_operacao(dados):
        OperacaoController.validar_operacao(dados)
        create_operacao(dados)
        print("Operação criada com sucesso!")

    @staticmethod
    def listar_operacoes():
        return get_operacoes()

    @staticmethod
    def atualizar_operacao(operacao_id, novos_dados):
        OperacaoController.validar_operacao(novos_dados)
        update_operacao(operacao_id, novos_dados)
        print(f"Operação {operacao_id} atualizada com sucesso!")

    @staticmethod
    def deletar_operacao(operacao_id):
        delete_operacao(operacao_id)
        print(f"Operação {operacao_id} deletada com sucesso!")
