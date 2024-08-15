#faca um progama que receba tres notas e seus respectivos pesos, calcule e faca a media aritimetica deles 
# Solicita ao usuário que insira três notas e seus respectivos pesos
nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))

# Calcula a média ponderada
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Exibe o resultado
print("A média ponderada das três notas é:", media_ponderada)

#nao entendi 