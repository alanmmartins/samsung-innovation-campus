# # Definindo uma função que recebe dois parâmetros e retorna a soma
# def somar(a, b):
#     return a + b

# # Chamando a função e imprimindo o resultado
# resultado = somar(5, 3)
# print(resultado)  # Saída: 8
# Exemplo 2: Função com Valor Padrão para Parâmetros
# python
# Copiar código
# # Definindo uma função com um valor padrão para um parâmetro
# def saudacao(nome, saudacao="Olá"):
#     return f"{saudacao}, {nome}!"

# # Chamando a função com e sem o parâmetro padrão
# print(saudacao("Ana"))                 # Saída: Olá, Ana!
# print(saudacao("Carlos", "Bom dia"))  # Saída: Bom dia, Carlos!
# Exemplo 3: Função com Número Variável de Argumentos
# python
# Copiar código
# # Definindo uma função que aceita um número variável de argumentos
# def imprimir_lista(*args):
#     for item in args:
#         print(item)

# # Chamando a função com diferentes números de argumentos
# imprimir_lista(1, 2, 3)         # Saída: 1\n2\n3
# imprimir_lista('a', 'b', 'c')   # Saída: a\nb\nc
# Exemplo 4: Função com Argumentos Nomeados (Keyword Arguments)
# python
# Copiar código
# # Definindo uma função que aceita argumentos nomeados
# def criar_usuario(nome, idade, email=None):
#     usuario = {
#         'nome': nome,
#         'idade': idade,
#         'email': email
#     }
#     return usuario

# # Chamando a função com e sem o argumento nomeado
# print(criar_usuario('Luís', 30))                  # Saída: {'nome': 'Luís', 'idade': 30, 'email': None}
# print(criar_usuario('Marta', 25, email='marta@example.com'))  # Saída: {'nome': 'Marta', 'idade': 25, 'email': 'marta@example.com'}
# Exemplo 5: Função com Valor de Retorno Múltiplo
# python
# Copiar código
# # Definindo uma função que retorna múltiplos valores
# def operacoes_basicas(a, b):
#     soma = a + b
#     subtracao = a - b
#     multiplicacao = a * b
#     divisao = a / b if b != 0 else 'Divisão por zero'
#     return soma, subtracao, multiplicacao, divisao

# # Chamando a função e recebendo múltiplos valores de retorno
# resultado = operacoes_basicas(10, 2)
# print(resultado)  # Saída: (12, 8, 20, 5.0)
# Exemplo 6: Função Lambda
# python
# Copiar código
# # Definindo uma função lambda que calcula o quadrado de um número
# quadrado = lambda x: x * x

# # Chamando a função lambda e imprimindo o resultado
# print(quadrado(4))  # Saída: 16
# Exemplo 7: Função com Documentação (Docstring)
# python
# Copiar código
# # Definindo uma função com uma docstring para documentação
# def potencia(base, expoente):
#     """
#     Calcula a potência de um número.
    
#     :param base: A base da potência
#     :param expoente: O expoente da potência
#     :return: O resultado da base elevada ao expoente
#     """
#     return base ** expoente

# # Chamando a função e imprimindo o resultado
# print(potencia(2, 3))  # Saída: 8

# # Imprimindo a docstring da função
# print(potencia.__doc__)  
# # Saída:
# # Calcula a potência de um número.
# # 
# # :param base: A base da potência
# # :param expoente: O expoente da potência
# # :return: O resultado da base elevada ao expoente
# Exemplo 8: Função Recursiva
# python
# Copiar código
# # Definindo uma função recursiva que calcula o fatorial de um número
# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n - 1)

# # Chamando a função e imprimindo o resultado
# print(fatorial(5))  # Saída: 120

# Exemplo 1: Função Simples com input()
# python
# Copiar código
# # Função que pede ao usuário para inserir dois números e retorna a soma
# def somar_numeros():
#     # Solicitando entradas do usuário
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
    
#     # Calculando a soma
#     resultado = num1 + num2
#     return resultado

# # Chamando a função e exibindo o resultado
# print("A soma é:", somar_numeros())
# Exemplo 2: Função com Entrada de Texto
# python
# Copiar código
# # Função que pede ao usuário para inserir seu nome e idade e retorna uma mensagem
# def saudacao_usuario():
#     nome = input("Qual é o seu nome? ")
#     idade = input("Quantos anos você tem? ")
    
#     mensagem = f"Olá, {nome}! Você tem {idade} anos."
#     return mensagem

# # Chamando a função e exibindo a mensagem
# print(saudacao_usuario())
# Exemplo 3: Função com Validação de Entrada
# python
# Copiar código
# # Função que solicita ao usuário um número e verifica se é positivo
# def verificar_numero_positivo():
#     while True:
#         try:
#             numero = float(input("Digite um número positivo: "))
#             if numero > 0:
#                 return f"O número {numero} é positivo."
#             else:
#                 print("O número deve ser positivo. Tente novamente.")
#         except ValueError:
#             print("Entrada inválida. Por favor, digite um número.")

# # Chamando a função e exibindo o resultado
# print(verificar_numero_positivo())
# Exemplo 4: Função com Múltiplas Entradas
# python
# Copiar código
# # Função que solicita ao usuário uma lista de números e retorna a média
# def calcular_media():
#     entrada = input("Digite uma lista de números separados por espaço: ")
#     numeros = entrada.split()  # Divide a string em uma lista de substrings
    
#     # Convertendo cada substring para float
#     numeros = [float(num) for num in numeros]
    
#     media = sum(numeros) / len(numeros)
#     return media

# # Chamando a função e exibindo a média
# print("A média dos números é:", calcular_media())
# Exemplo 5: Função com input() e Manipulação de Strings
# python
# Copiar código
# # Função que solicita ao usuário uma frase e retorna o número de palavras
# def contar_palavras():
#     frase = input("Digite uma frase: ")
#     palavras = frase.split()  # Divide a frase em uma lista de palavras
    
#     return f"A frase contém {len(palavras)} palavras."

# # Chamando a função e exibindo o resultado
# print(contar_palavras())
# Exemplo 6: Função Recursiva com Entrada do Usuário
# python
# Copiar código
# # Função recursiva que calcula a soma dos números até um número inserido pelo usuário
# def soma_recursiva(n):
#     if n <= 1:
#         return n
#     else:
#         return n + soma_recursiva(n - 1)

# def solicitar_numero():
#     while True:
#         try:
#             numero = int(input("Digite um número inteiro positivo para calcular a soma: "))
#             if numero > 0:
#                 return soma_recursiva(numero)
#             else:
#                 print("O número deve ser positivo. Tente novamente.")
#         except ValueError:
#             print("Entrada inválida. Por favor, digite um número inteiro.")

# # Chamando a função e exibindo o resultado
# print("A soma dos números até o número inserido é:", solicitar_numero())

# Exemplo 1: Função com Parâmetros Padrão Simples
# python
# Copiar código
# # Função que saudará o usuário com uma saudação padrão se não for fornecida uma
# def saudacao(nome="Usuário", saudacao="Olá"):
#     return f"{saudacao}, {nome}!"

# # Chamando a função sem argumentos, com o valor padrão
# print(saudacao())  # Saída: Olá, Usuário!

# # Chamando a função com um argumento
# print(saudacao("Ana"))  # Saída: Olá, Ana!

# # Chamando a função com dois argumentos
# print(saudacao("Carlos", "Bom dia"))  # Saída: Bom dia, Carlos!
# Exemplo 2: Função com Parâmetros Padrão e input()
# python
# Copiar código
# # Função que solicita o nome do usuário e retorna uma saudação com um valor padrão para a saudação
# def saudacao_usuario(nome=None, saudacao="Olá"):
#     if nome is None:
#         nome = input("Qual é o seu nome? ")
#     return f"{saudacao}, {nome}!"

# # Chamando a função sem fornecer o nome (usará `input()`)
# print(saudacao_usuario(saudacao="Bom dia"))  

# # Chamando a função fornecendo o nome diretamente
# print(saudacao_usuario(nome="Ana", saudacao="Boa tarde"))  
# Exemplo 3: Função com Parâmetros Padrão para Processamento de Dados
# python
# Copiar código
# # Função que solicita uma lista de números e calcula a média, com valor padrão para o separador
# def calcular_media(separador=" ", entrada=None):
#     if entrada is None:
#         entrada = input("Digite uma lista de números separados por espaços: ")
    
#     numeros = entrada.split(separador)  # Divide a string em uma lista de substrings
#     numeros = [float(num) for num in numeros]  # Converte cada substring para float
    
#     if len(numeros) == 0:
#         return "Nenhum número fornecido."
    
#     media = sum(numeros) / len(numeros)
#     return media

# # Chamando a função com entrada fornecida diretamente
# print(calcular_media(entrada="10 20 30", separador=" "))

# # Chamando a função sem fornecer entrada (usará `input()`)
# print("A média dos números é:", calcular_media())
# Exemplo 4: Função com Parâmetros Padrão e Validação
# python
# Copiar código
# # Função que solicita um número e verifica se é positivo, com valor padrão para o prompt
# def verificar_numero_positivo(prompt="Digite um número positivo: ", limite=None):
#     while True:
#         try:
#             numero = float(input(prompt))
#             if numero > limite:
#                 return f"O número {numero} é válido."
#             else:
#                 print(f"O número deve ser maior que {limite}. Tente novamente.")
#         except ValueError:
#             print("Entrada inválida. Por favor, digite um número.")

# # Chamando a função com valores padrão
# print(verificar_numero_positivo())

# # Chamando a função com um limite personalizado
# print(verificar_numero_positivo(limite=10))
# Exemplo 5: Função Recursiva com Parâmetros Padrão
# python
# Copiar código
# # Função recursiva para calcular a soma até um número fornecido, com limite padrão
# def soma_recursiva(n, limite=0):
#     if n <= limite:
#         return limite
#     else:
#         return n + soma_recursiva(n - 1, limite)

# def solicitar_numero(limite=0):
#     while True:
#         try:
#             numero = int(input("Digite um número inteiro positivo para calcular a soma: "))
#             if numero > limite:
#                 return soma_recursiva(numero, limite)
#             else:
#                 print(f"O número deve ser maior que {limite}. Tente novamente.")
#         except ValueError:
#             print("Entrada inválida. Por favor, digite um número inteiro.")

# # Chamando a função com limite padrão
# print("A soma dos números até o número inserido é:", solicitar_numero())

# # Chamando a função com limite personalizado
# print("A soma dos números até o número inserido, com limite 5 é:", solicitar_numero(limite=5))