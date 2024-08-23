# Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a área
# do terreno.
def área(largura, comprimento):

    return largura * comprimento

# comp largura
largura = int(input("Digite a largura do terreno: "))
comprimento = int(input("Digite o comprimento do terreno: "))


resultado = área(largura, comprimento)

print(f"A área do terreno é: {resultado:.2f} metros ")
