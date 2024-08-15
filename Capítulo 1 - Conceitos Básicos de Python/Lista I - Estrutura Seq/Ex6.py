#faca um programa em python que receba o salario-base de um funcionario, calcule e mostre o salario a receber sabendo-se que esse funcionario tem gratificacao de 5% sobre o salario base e paga imposto de 7%sobre o salario base 

# Solicita ao usuário que insira o salário-base do funcionário
salario_base = float(input("Digite o salário-base do funcionário: "))

# Calcula a gratificação de 5% sobre o salário-base
gratificacao = salario_base * 0.05

# Calcula o imposto de 7% sobre o salário-base
imposto = salario_base * 0.07

# Calcula o salário a receber
salario_a_receber = salario_base + gratificacao - imposto

# Exibe o resultado
print("O salário a receber do funcionário é:", salario_a_receber)
