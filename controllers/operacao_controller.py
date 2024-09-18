from astra_api import create_operacao, get_operacoes, update_operacao, delete_operacao
from datetime import datetime

class OperacaoController:

    @staticmethod
    def validar_operacao(dados):
        # Verificar se o ID da reserva está presente
        if "reserva_id" not in dados or not dados["reserva_id"]:
            raise ValueError("ID da reserva é obrigatório")
        
        # Verificar se o tipo de operação é válido (agora usando 'tipo_operacao')
        if "tipo_operacao" not in dados or dados["tipo_operacao"] not in ["check-in", "check-out"]:
            raise ValueError("Tipo de operação inválido")  
        
        # Verificar se a data da operação está presente
        if "data_operacao" not in dados or not dados["data_operacao"]:
            raise ValueError("Data e hora da operação são obrigatórias")
    
    @staticmethod
    def criar_operacao(dados):
        # Validar os dados antes da criação
        OperacaoController.validar_operacao(dados)
        create_operacao(dados)
        print("Operação criada com sucesso!")

    @staticmethod
    def listar_operacoes():
        # Listar todas as operações
        return get_operacoes()

    @staticmethod
    def atualizar_operacao(operacao_id, novos_dados):
        # Validar os novos dados antes de atualizar a operação
        OperacaoController.validar_operacao(novos_dados)
        update_operacao(operacao_id, novos_dados)
        print(f"Operação {operacao_id} atualizada com sucesso!")

    @staticmethod
    def deletar_operacao(operacao_id):
        # Deletar a operação com base no ID
        delete_operacao(operacao_id)
        print(f"Operação {operacao_id} deletada com sucesso!")
