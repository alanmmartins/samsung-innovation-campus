#faca um programa que receba o salario-base de um funcionario, calcule e mostre o seu salario a receber sabendo-se que esse funcionario tem gratificacao de R$50,00 e paga imposto de 10% sobre o salario base

# Solicita ao usuário que insira o salário-base do funcionário
salario_base = float(input("Digite o salário-base do funcionário: "))

# Define a gratificação fixa de R$50,00
gratificacao = 50.00

# Calcula o imposto de 10% sobre o salário-base
imposto = salario_base * 0.10

# Calcula o salário a receber
salario_a_receber = salario_base + gratificacao - imposto

# Exibe o resultado
print("O salário a receber do funcionário é:", salario_a_receber)
