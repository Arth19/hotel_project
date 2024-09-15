from mongo_api import get_hospedes

# Teste para buscar os hóspedes
def testar_get_hospedes():
    hospedes = get_hospedes()
    if hospedes:
        print("Hóspedes encontrados:")
        for hospede in hospedes:
            print(hospede)
    else:
        print("Nenhum hóspede encontrado.")

# Executa o teste
if __name__ == "__main__":
    testar_get_hospedes()
