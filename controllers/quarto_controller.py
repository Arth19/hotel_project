# controllers/quarto_controller.py
from mongo_api import create_quarto, get_quartos, update_quarto, delete_quarto

class QuartoController:

    @staticmethod
    def validar_quarto(dados):
        if "numero_quarto" not in dados or not dados["numero_quarto"]:
            raise ValueError("Número do quarto é obrigatório")
        
        if "tipo" not in dados or not dados["tipo"]:
            raise ValueError("Tipo do quarto é obrigatório")
        
        if "preco_diaria" not in dados or dados["preco_diaria"] <= 0:
            raise ValueError("Preço da diária deve ser um valor positivo")

    @staticmethod
    def criar_quarto(dados):
        # Validar dados antes da criação
        QuartoController.validar_quarto(dados)
        create_quarto(dados)
        print("Quarto criado com sucesso!")

    @staticmethod
    def listar_quartos():
        return get_quartos()

    @staticmethod
    def atualizar_quarto(quarto_id, novos_dados):
        # Validar os novos dados antes da atualização
        QuartoController.validar_quarto(novos_dados)
        update_quarto(quarto_id, novos_dados)
        print(f"Quarto {quarto_id} atualizado com sucesso!")

    @staticmethod
    def deletar_quarto(quarto_id):
        delete_quarto(quarto_id)
        print(f"Quarto {quarto_id} deletado com sucesso!")
