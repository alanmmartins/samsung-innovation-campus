# Função com input() e Manipulação de Strings

def contar_palavras():
     frase = input("Digite uma frase: ")
     palavras = frase.split()  # Divide a frase em uma lista de palavras
    
     return f"A frase contém {len(palavras)} palavras."
print(contar_palavras())