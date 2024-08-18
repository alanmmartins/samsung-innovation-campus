# Função com Múltiplas Entradas

def calcular_media():
    entrada = input("Digite uma lista de números separados por espaço: ")
    numeros = entrada.split()  # Divide a string em uma lista de substrings
    
# Convertendo cada substring para float
    numeros = [float(num) for num in numeros]
    
    media = sum(numeros) / len(numeros)
    return media

 # Chamando a função e exibindo a média
print("A média dos números é:", calcular_media())