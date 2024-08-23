# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.

def maior(numeros):
    if len(numeros) == 0:
        print("Nenhum número foi fornecido.")
    else:
        maior_num = max(numeros)
        print(f"O maior número entre {numeros} é {maior_num}.")


entrada = input("Digite os números inteiros separados por espaço: ")

numeros = tuple(map(int, entrada.split()))


maior(numeros)



