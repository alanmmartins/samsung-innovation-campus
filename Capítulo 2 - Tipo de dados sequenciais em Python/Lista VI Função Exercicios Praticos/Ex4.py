# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
# os valores pares sorteados pela função anterior.
import random

numeros = []

def sorteia():
    for _ in range(5):
        num = random.randint(1, 100)
        numeros.append(num)
    print(f"Números sorteados: {numeros}")

def somaPar():

    soma = sum(num for num in numeros if num % 2 == 0)
    print(f"Soma dos números pares: {soma}")

sorteia()
somaPar()


