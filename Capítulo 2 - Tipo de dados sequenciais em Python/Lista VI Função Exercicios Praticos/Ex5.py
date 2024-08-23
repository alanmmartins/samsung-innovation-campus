# Crie um programa que tenha uma função fatorial() e retorno o valor fatorial de
# três variáveis em tela.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o  segundo número: "))
num3 = int(input('Digite o terceiro número: '))


fatorial1 = fatorial(num1)
fatorial2 = fatorial(num2)
fatorial3 = fatorial(num3)


print(f"Fatorial de {num1} é {fatorial1}")
print(f"Fatorial de {num2} é {fatorial2}")
print(f"Fatorial de {num3} é {fatorial3}")


