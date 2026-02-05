
def calcular_idade():
    nome_completo = input("Digite seu nome completo: ")
    
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            
            if 1922 <= ano_nascimento <= 2021:
                idade = 2022 - ano_nascimento
                print(f"\nNome: {nome_completo}")
                print(f"Idade completada (ou a completar) em 2022: {idade} anos")
                break
            else:
                print("Erro: O ano deve estar entre 1922 e 2021. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, digite um número válido para o ano.")

if __name__ == "__main__":
    calcular_idade()
