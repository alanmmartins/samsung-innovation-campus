#Faça um programa que, no momento de preencher um vetor com oito números
#inteiros, já os armazene de forma crescente.

def insere_ordenado(vetor, num):
    i = 0
    while i < len(vetor) and vetor[i] < num:
        i += 1
    vetor.insert(i, num)

def insere_ordenado(vetor, num):
    # Inicia a função insere_ordenado, que recebe um vetor e um número (num).
    
    i = 0
    # Define o índice 'i' como 0. Esse índice será usado para encontrar a posição correta para inserir o número.
    
    while i < len(vetor) and vetor[i] < num:
        # Enquanto 'i' for menor que o comprimento do vetor e o valor no vetor na posição 'i' for menor que 'num':
        
        i += 1
        # Incrementa 'i' para avançar para a próxima posição no vetor.
    
    vetor.insert(i, num)
    # Insere 'num' na posição 'i' do vetor, o que mantém o vetor em ordem crescente.

def preenche_vetor_crescente():
    # Inicia a função preenche_vetor_crescente, que preenche o vetor com oito números em ordem crescente.
    
    vetor = []
    # Cria um vetor vazio que armazenará os números em ordem crescente.
    
    for _ in range(8):
        # Laço que se repetirá 8 vezes, para preencher o vetor com oito números.
        
        while True:
            # Inicia um laço infinito que continuará até que um número válido seja inserido.
            
            try:
                # Tenta executar o bloco de código abaixo.
                
                num = int(input("Digite um número inteiro: "))
                # Solicita ao usuário que insira um número inteiro e tenta converter a entrada para um número inteiro.
                
                break
                # Se a conversão for bem-sucedida, sai do laço while.
                
            except ValueError:
                # Se houver um erro ao tentar converter a entrada (ou seja, se o usuário não digitou um número inteiro):
                
                print("Por favor, digite um valor inteiro válido.")
                # Exibe uma mensagem de erro ao usuário, pedindo um número inteiro válido.
        
        insere_ordenado(vetor, num)
        # Chama a função insere_ordenado para inserir o número 'num' no vetor na posição correta.
    
    return vetor
    # Retorna o vetor preenchido em ordem crescente.

# Executando a função
vetor_crescente = preenche_vetor_crescente()
# Chama a função preenche_vetor_crescente e armazena o vetor ordenado na variável 'vetor_crescente'.

print("Vetor em ordem crescente:", vetor_crescente)
# Imprime o vetor em ordem crescente.