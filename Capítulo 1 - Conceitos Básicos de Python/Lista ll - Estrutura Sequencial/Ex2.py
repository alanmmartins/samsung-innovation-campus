#faca um progama em python que receba dois numeros maiores que zero,calcule e mostre um elevado ao outro

# Solicita ao usuário que insira dois números maiores que zero
numero1 = int(input("Digite o primeiro número maior que zero: "))
numero2 = int(input("Digite o segundo número maior que zero: "))

# Verifica se ambos os números são maiores que zero
if numero1 <= 0 or numero2 <= 0:
    print("Ambos os números devem ser maiores que zero.")
else:
    # Calcula o primeiro número elevado ao segundo
    resultado = numero1 ** numero2

    # Exibe o resultado
    print(f"{numero1} elevado a {numero2} é igual a {resultado}")
