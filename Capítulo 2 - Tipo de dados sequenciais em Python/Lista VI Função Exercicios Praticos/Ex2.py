# Faça um programa que tenha uma função chamada contador(), que receba
# duas parâmetros: início, fim e passo. Seu programa tem que realizar três
# contagens através da função criada:
# • de 1 até 10, de 1 em 1;
# • de 10 até 0, de 2 em 2

def contador(inicio, fim, passo):

    if passo == 0:
        print('passo nâo podemser zero')
        return

    if inicio < fim:

        for i in range(inicio, fim + 1, passo):
            print(i)
    else:

        for i in range(inicio, fim - 1, -passo):
            print(i)
    print()

print(" 1 até 10, de 1 em 1:")
contador(1, 10, 1)

print("Contagem de 10 até 0, de 2 em 2:")
contador(10, 0, 2)
