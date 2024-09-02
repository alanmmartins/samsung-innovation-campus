def soma_intervalo(m, n):
    soma = 0
    for i in range(m, n + 1):
        soma += i
    return soma

def main():
    while True:
        m = int(input("Digite o valor de m: "))
        n = int(input("Digite o valor de n: "))

        if m < n:
            resultado = soma_intervalo(m, n)
            print("Soma dos números de", m, "até", n, "é:", resultado)
        else:
            print("m não é menor que n. O loop foi encerrado.")
            break

if __name__ == "__main__":
    main()
