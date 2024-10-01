# ALGORITMO
# DECLARE m, n, soma, i NUMÉRICO
# LEIA m
# LEIA n
# ENQUANTO m < n FAÇA
# INÍCIO
# soma ← 0
# PARA i m ATÉ n FAÇA
# INÍCIO
# soma ← soma + i
# FIM
# ESCREVA soma
# LEIA m
# LEIA n
# FIM

def calcular_soma_intervalos():
    # Lendo os valores de m e n
    m = int(input("Digite o valor de m: "))
    n = int(input("Digite o valor de n: "))

    # Loop para repetir enquanto m for menor que n
    while m < n:
        soma = 0
        
        # Calculando a soma de m até n
        for i in range(m, n + 1):
            soma += i
        
        # Exibindo o resultado
        print(f"Soma dos números de {m} a {n}: {soma}")
        
        # Lendo os novos valores de m e n
        m = int(input("Digite o valor de m: "))
        n = int(input("Digite o valor de n: "))

# Executando o algoritmo
calcular_soma_intervalos()
