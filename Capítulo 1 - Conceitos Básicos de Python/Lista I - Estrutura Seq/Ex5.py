#faca um programa que receba o salario de um funcionario e o percentual de aumento, calcule e mostre o valor do aumento e o novo salario

# Solicita ao usuário que insira o salário atual do funcionário
salario_atual = float(input("Digite o salário atual do funcionário: "))

# Solicita ao usuário que insira o percentual de aumento
percentual_aumento = float(input("Digite o percentual de aumento (por exemplo, 25 para 25%): "))

# Calcula o valor do aumento
valor_aumento = salario_atual * (percentual_aumento / 100)

# Calcula o novo salário
novo_salario = salario_atual + valor_aumento

# Exibe o valor do aumento e o novo salário
print("O valor do aumento é:", valor_aumento)
print("O novo salário do funcionário é:", novo_salario)
