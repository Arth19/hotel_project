from astra_api import create_faturamento, get_faturamentos, update_faturamento, delete_faturamento

class FaturamentoController:

    @staticmethod
    def validar_faturamento(dados):
        # Verificar se o ID da reserva está presente
        if "reserva_id" not in dados or not dados["reserva_id"]:
            raise ValueError("ID da reserva é obrigatório")
        
        # Verificar se o valor total é válido
        if "valor_total" not in dados or dados["valor_total"] <= 0:
            raise ValueError("Valor total do faturamento deve ser maior que zero")
        
        # Verificar o método de pagamento
        if "metodo_pagamento" not in dados or dados["metodo_pagamento"] not in ["cartao_credito", "boleto", "transferencia"]:
            raise ValueError("Método de pagamento inválido")

        # Verificar se a data de pagamento está presente
        if "data_pagamento" not in dados or not dados["data_pagamento"]:
            raise ValueError("Data de pagamento é obrigatória")

    @staticmethod
    def criar_faturamento(dados):
        # Validar os dados antes de criar o faturamento
        FaturamentoController.validar_faturamento(dados)
        create_faturamento(dados)
        print("Faturamento criado com sucesso!")

    @staticmethod
    def listar_faturamentos():
        # Retornar a lista de faturamentos
        return get_faturamentos()

    @staticmethod
    def atualizar_faturamento(faturamento_id, novos_dados):
        # Validar os novos dados antes de atualizar o faturamento
        FaturamentoController.validar_faturamento(novos_dados)
        update_faturamento(faturamento_id, novos_dados)
        print(f"Faturamento {faturamento_id} atualizado com sucesso!")

    @staticmethod
    def deletar_faturamento(faturamento_id):
        # Deletar o faturamento com base no ID
        delete_faturamento(faturamento_id)
        print(f"Faturamento {faturamento_id} deletado com sucesso!")
