# Desenhe um fluxograma da fatoração dos números 18, 39, 63, 126, 792

def fatoracao(n):
    # Define a função 'fatoracao' que recebe um número 'n' como argumento.
    
    fatores = []
    # Inicializa uma lista vazia 'fatores' para armazenar os fatores primos de 'n'.
    
    divisor = 2
    # Define o primeiro divisor como 2, o menor número primo.
    
    while n > 1:
        # Continua o loop enquanto 'n' for maior que 1.
        
        while n % divisor == 0:
            # Enquanto 'n' for divisível pelo 'divisor' atual (ou seja, o resto da divisão for 0):
            
            fatores.append(divisor)
            # Adiciona o 'divisor' à lista de fatores.
            
            n //= divisor
            # Divide 'n' pelo 'divisor' e atualiza 'n' com o resultado da divisão inteira.
        
        divisor += 1
        # Incrementa o 'divisor' em 1 para testar o próximo número.
    
    return fatores
    # Retorna a lista de fatores primos de 'n'.

numeros = [18, 39, 63, 126, 792]
# Define uma lista de números para fatorar.

for numero in numeros:
    # Itera sobre cada número na lista 'numeros'.
    
    print(f"Fatores de {numero}: {fatoracao(numero)}")
    # Imprime os fatores primos de cada número usando a função 'fatoracao'.
    #O f antes das aspas indica uma f-string (string formatada) em Python. Isso permite incluir expressões dentro de chaves {} que serão avaliadas e formatadas como parte da string.

# def fatoracao(n, divisor=2, fatores=None):
#     if fatores is None:
#         fatores = []
#     if n <= 1:
#         return fatores
#     if n % divisor == 0:
#         fatores.append(divisor)
#         return fatoracao(n // divisor, divisor, fatores)
#     else:
#         return fatoracao(n, divisor + 1, fatores)

# numeros = [18, 39, 63, 126, 792]
# for numero in numeros:
#     print(f"Fatores de {numero}: {fatoracao(numero)}")    