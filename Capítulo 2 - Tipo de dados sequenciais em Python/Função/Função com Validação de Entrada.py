#  Função com Validação de Entrada

def verificar_numero_positivo():
     while True:
         try:
             numero = float(input("Digite um número qualquer"))
             if numero > 0:
                 return f"O número {numero} é positivo."
             else:
                 print("O número deve ser positivo. Tente novamente.")
         except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


print(verificar_numero_positivo())