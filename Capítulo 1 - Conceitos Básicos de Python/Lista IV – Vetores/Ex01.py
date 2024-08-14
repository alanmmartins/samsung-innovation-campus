#Faça um programa que, no momento de preencher um vetor com oito números
#inteiros, já os armazene de forma crescente.

def insere_ordenado(vetor, num):
    i = 0
    while i < len(vetor) and vetor[i] < num:
        i += 1
    vetor.insert(i, num)

def preenche_vetor_crescente():
    vetor = []
    for _ in range(8):
        num = int(input("Digite um número inteiro: "))
        insere_ordenado(vetor, num)
    return vetor

# Executando a função
vetor_crescente = preenche_vetor_crescente()
print("Vetor em ordem crescente:", vetor_crescente)