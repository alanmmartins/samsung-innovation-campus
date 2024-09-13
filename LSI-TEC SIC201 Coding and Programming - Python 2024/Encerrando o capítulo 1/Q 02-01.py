# Escreva um programa que imprima a soma dos números ÍMPARES de 1 a 100. A lógica do programa é representada pelo diagrama de fluxo abaixo.
# Inicializa a variável que vai armazenar a soma dos números ímpares
soma = 0

# Percorre todos os números de 1 a 100
for i in range(1, 101):
    # Verifica se o número é ímpar
    if i % 2 != 0:
        # Adiciona o número ímpar à soma
        soma += i

# Imprime a soma dos números ímpares
print("A soma dos números ímpares de 1 a 100 é:", soma)
