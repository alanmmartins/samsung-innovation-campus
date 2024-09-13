# Um número Armstrong é um número inteiro de três dígitos que é igual à soma dos cubos de cada dígito. Encontre todos os números Armstrong entre números inteiros de três dígitos e imprima-os.

# Exemplo: 

# 153 é um número Armstrong, pois 1³+5³+3³ = 1+125+27 = 153

# Função para verificar se um número é um número Armstrong
def is_armstrong(number):
    # Convertemos o número para string para acessar cada dígito
    digits = str(number)
    # Calculamos a soma dos cubos dos dígitos
    sum_of_cubes = sum(int(digit) ** 3 for digit in digits)
    # Verificamos se a soma é igual ao número original
    return sum_of_cubes == number

# Encontrar e imprimir todos os números Armstrong de três dígitos
for num in range(100, 1000):
    if is_armstrong(num):
        print(num)
