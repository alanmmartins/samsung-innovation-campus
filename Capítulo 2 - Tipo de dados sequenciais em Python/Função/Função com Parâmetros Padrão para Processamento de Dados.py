# Função com Parâmetros Padrão para Processamento de Dados
def calcular_media(separador=" ", entrada=None):
     if entrada is None:
         entrada = input("Digite uma lista de números separados por espaços: ")
    
     numeros = entrada.split(separador)  # Divide a string em uma lista de substrings
     numeros = [int(num) for num in numeros] 
    
     if len(numeros) == 0:
         return "Nenhum número fornecido."
    
     media = sum(numeros) / len(numeros)
     return media

print("A média dos números é:", calcular_media())