# Escreva um programa que recebe um número inteiro positivo do usuário e diz se é um número par ou ímpar. Use o pseudo-código para se guiar:



# print 'Digite um número inteiro positivo:'
# n = input()
# se resto da divisão por 2 é igual a 0:
#     print 'n é par'
# se não:
#     print 'n é ímpar'

# Solicita ao usuário que digite um número inteiro positivo
print('Digite um número inteiro positivo:')
n = int(input())  # Lê a entrada e converte para um número inteiro

# Verifica se o número é par ou ímpar
if n % 2 == 0:
    print(f'{n} é par')
else:
    print(f'{n} é ímpar')
