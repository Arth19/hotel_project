from astra_api import create_faturamento, get_faturamentos, update_faturamento, delete_faturamento

class FaturamentoController:

    @staticmethod
    def validar_faturamento(dados):
        if "reserva_id" not in dados or not dados["reserva_id"]:
            raise ValueError("ID da reserva é obrigatório")
        
        if "valor_total" not in dados or dados["valor_total"] <= 0:
            raise ValueError("Valor total deve ser um valor positivo")
        
        if "metodo_pagamento" not in dados or dados["metodo_pagamento"] not in ["cartao", "dinheiro", "transferencia"]:
            raise ValueError("Método de pagamento inválido")

    @staticmethod
    def criar_faturamento(dados):
        FaturamentoController.validar_faturamento(dados)
        create_faturamento(dados)
        print("Faturamento criado com sucesso!")

    @staticmethod
    def listar_faturamentos():
        return get_faturamentos()

    @staticmethod
    def atualizar_faturamento(faturamento_id, novos_dados):
        FaturamentoController.validar_faturamento(novos_dados)
        update_faturamento(faturamento_id, novos_dados)
        print(f"Faturamento {faturamento_id} atualizado com sucesso!")

    @staticmethod
    def deletar_faturamento(faturamento_id):
        delete_faturamento(faturamento_id)
        print(f"Faturamento {faturamento_id} deletado com sucesso!")
