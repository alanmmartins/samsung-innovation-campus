#faca um programa em python que receba o salario de um funcionario, calcule e mostre o novo salario ,sabendo que sofreu um aumento de 25%

# Solicita ao usuário que insira o salário atual do funcionário
salario_atual = float(input("Digite o salário atual do funcionário: "))

# Calcula o novo salário com o aumento de 25%
aumento = 25 / 100
novo_salario = salario_atual * (1 + aumento)

# Exibe o resultado
print("O novo salário do funcionário, com aumento de 25%, é:", novo_salario)
