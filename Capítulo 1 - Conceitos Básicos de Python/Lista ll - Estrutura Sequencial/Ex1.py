#faca um programa em python eque receba um numero positivo maior que zero,calcule e mostre : 
#a)o numero digitado ao quadrado
#b)o numero digitado ao cubo 
#c)a raiz quadrada do numero digitado
#d)a raiz cubica do numero digitado

# Solicita ao usuário que insira um número positivo maior que zero
numero = int(input("Digite um número positivo maior que zero: "))

# Verifica se o número é positivo
if numero <= 0:
    print("O número deve ser positivo e maior que zero.")
else:
    # Calcula o número ao quadrado
    quadrado = numero ** 2

    # Calcula o número ao cubo
    cubo = numero ** 3

    # Calcula a raiz quadrada do número
    raiz_quadrada = numero ** 0.5

    # Calcula a raiz cúbica do número
    raiz_cubica = numero ** (1/3)

    # Exibe os resultados
    print("O número ao quadrado é:", quadrado)
    print("O número ao cubo é:", cubo)
    print("A raiz quadrada do número é:", raiz_quadrada)
    print("A raiz cúbica do número é:", raiz_cubica)
