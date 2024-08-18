#Função Lambda
quadrado = lambda x: x * x
print(quadrado(4))  


soma = lambda x, y: x + y
resultado = soma(10, 6)
print(resultado)  


# Lista de números
numeros = [1, 1, 2, 2, 2]
# Multiplica cada número por 2 usando lambda e map
dobro = list(map(lambda x: x * 2, numeros))
print(dobro)  


# Lista de números
numeros = [1, 15, 3, 11, 5, 13, 7, 17, 9, 16]
# Filtra números pares usando lambda e filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) 

# Lista de tuplas
pessoas = [('João', 25), ('Maria', 22), ('alan', 30)]
# Ordena a lista pela idade (segundo elemento da tupla)
ordenado_por_idade = sorted(pessoas, key=lambda x: x[1])
print(ordenado_por_idade)  

# Ordena a lista pela idade (PRIMEIRO elemento da tupla)
pessoas = [('João', 25), ('Maria', 22), ('Alan', 30)]
ordenado_por_nome = sorted(pessoas, key=lambda x: x[0]) #INDEX 0 1 ELEMENT
print(ordenado_por_nome)