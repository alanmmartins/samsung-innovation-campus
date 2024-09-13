# Entre os números naturais positivos diferentes de 1, um número que não é primo é chamado de número composto. Imprima os números primos e compostos de 2 a 12.

# Uma expressão deve determinar se o número é primo ou composto, caso seja composto, deve ser impresso na tela.

import math

def is_prime(n):
    """Retorna True se n for um número primo, caso contrário, retorna False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Imprime os números primos e compostos entre 2 e 12
for num in range(2, 13):
    if is_prime(num):
        print(f"{num} é primo")
    else:
        print(f"{num} é composto")
