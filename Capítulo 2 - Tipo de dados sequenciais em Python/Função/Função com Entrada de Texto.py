#  Função com Entrada de Texto


def usuario():
     nome = input("Qual é o seu nome? ")
     idade = int(input("Quantos anos você tem? "))
    
     mensagem = f"Olá, {nome}! Você tem {idade} anos."
     return mensagem

print(usuario())