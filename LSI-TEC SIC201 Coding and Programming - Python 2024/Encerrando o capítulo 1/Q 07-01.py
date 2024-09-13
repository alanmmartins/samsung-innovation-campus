# Função para ler e validar dois números inteiros diferentes
def ler_e_validar_numeros():
    while True:
        try:
            # Solicita a entrada do usuário
            entrada = input("Insira dois números inteiros: ")
            # Divide a entrada em duas partes
            num1, num2 = map(int, entrada.split())
            
            # Verifica se os números são diferentes
            if num1 != num2:
                return num1, num2
            else:
                print("Os números devem ser diferentes. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira dois números inteiros separados por espaço.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Função principal do programa
def main():
    num1, num2 = ler_e_validar_numeros()
    
    # Ordena os números e imprime na ordem crescente
    menor, maior = sorted([num1, num2])
    print(f"Os números inseridos em ordem crescente são: {menor} {maior}")

# Executa o programa
if __name__ == "__main__":
    main()
