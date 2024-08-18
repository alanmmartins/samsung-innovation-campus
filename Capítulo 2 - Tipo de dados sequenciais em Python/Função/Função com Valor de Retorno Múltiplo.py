#Função com Valor de Retorno Múltiplo

def operacoes_basicas(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else 'Divisão por zero'
    return soma, subtracao, multiplicacao, divisao

# Solicita ao usuário que insira os valores de a e b
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))

resultado = operacoes_basicas(a, b)
print(resultado)
print(f"Soma: {resultado[0]}")
print(f"Subtração: {resultado[1]}")
print(f"Multiplicação: {resultado[2]}")
print(f"Divisão: {resultado[3]}")

