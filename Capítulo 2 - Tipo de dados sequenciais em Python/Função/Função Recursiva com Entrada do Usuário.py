# Função Recursiva com Entrada do Usuário

def soma_recursiva(n):
     if n <= 1:
         return n
     else:
         return n + soma_recursiva(n - 1)

def solicitar_numero():
     while True:
         try:
             numero = int(input("Digite um número inteiro positivo para calcular a soma: "))
             if numero > 0:
                 return soma_recursiva(numero)
             else:
                 print("O número deve ser positivo. Tente novamente.")
         except ValueError:
             print("Entrada inválida. Por favor, digite um número inteiro.")

print("A soma dos números até o número inserido é:", solicitar_numero())
