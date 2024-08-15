#faca um programa em python receba o valor de um deposito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento

# Solicita ao usuário que insira o valor do depósito
deposito = float(input("Digite o valor do depósito: "))

# Solicita ao usuário que insira a taxa de juros (em porcentagem)
taxa_juros = float(input("Digite a taxa de juros (por exemplo, 5 para 5%): "))

# Calcula o valor do rendimento
rendimento = deposito * (taxa_juros / 100)

# Calcula o valor total após o rendimento
valor_total = deposito + rendimento

# Exibe o valor do rendimento e o valor total
print("O valor do rendimento é:", rendimento)
print("O valor total após o rendimento é:", valor_total)
