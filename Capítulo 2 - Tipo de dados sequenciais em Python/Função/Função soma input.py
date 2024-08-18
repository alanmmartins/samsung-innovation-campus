# Função Simples com input()
def soma(a,b):
  resul = a + b
  return resul

x = int(input("Informe o primeiro Valor: "))
y = int(input("Informe o segundo valor: "))
resultado = soma(x,y)
print("Resultado: ", resultado)

#mais facil
def somar_numeros():
   
     num1 = int(input("Digite o primeiro número: "))
     num2 = int(input("Digite o segundo número: "))
    
    
     resultado = num1 + num2
     return resultado

print("A soma é:", somar_numeros())