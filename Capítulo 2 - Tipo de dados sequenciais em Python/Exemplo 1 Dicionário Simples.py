# Exemplo 1: Dicionário Simples
# python
# Copiar código
# # Criando um dicionário
# pessoa = {
#     'nome': 'Ana',
#     'idade': 28,
#     'cidade': 'São Paulo'
# }

# # Acessando um valor pelo chave
# print(pessoa['nome'])  # Saída: Ana
# print(pessoa['idade']) # Saída: 28

# # Adicionando um novo par chave-valor
# pessoa['email'] = 'ana@example.com'

# # Modificando um valor existente
# pessoa['idade'] = 29

# # Removendo um par chave-valor
# del pessoa['cidade']

# print(pessoa)  # Saída: {'nome': 'Ana', 'idade': 29, 'email': 'ana@example.com'}
# Exemplo 2: Dicionário com Tipos de Dados Variados
# python
# Copiar código
# # Criando um dicionário com diferentes tipos de dados
# produto = {
#     'id': 101,
#     'nome': 'Laptop',
#     'preço': 2999.99,
#     'disponível': True,
#     'especificações': {
#         'processador': 'Intel i7',
#         'ram': '16GB',
#         'armazenamento': '512GB SSD'
#     }
# }

# # Acessando um valor em um dicionário aninhado
# print(produto['especificações']['processador'])  # Saída: Intel i7
# Exemplo 3: Dicionário com Listas como Valores
# python
# Copiar código
# # Criando um dicionário com listas como valores
# aluno = {
#     'nome': 'João',
#     'notas': [7.5, 8.0, 9.0],
#     'disciplinas': ['Matemática', 'Português', 'História']
# }

# # Acessando valores da lista
# print(aluno['notas'])          # Saída: [7.5, 8.0, 9.0]
# print(aluno['notas'][1])       # Saída: 8.0
# print(aluno['disciplinas'][2]) # Saída: História
# Exemplo 4: Iterando Sobre um Dicionário
# python
# Copiar código
# # Iterando sobre chaves e valores
# carro = {
#     'marca': 'Ford',
#     'modelo': 'Mustang',
#     'ano': 2022
# }

# for chave, valor in carro.items():
#     print(f'{chave}: {valor}')

# # Saída:
# # marca: Ford
# # modelo: Mustang
# # ano: 2022
# Exemplo 5: Dicionário com Chaves de Tipos Diferentes
# python
# Copiar código
# # Criando um dicionário com diferentes tipos de chaves
# dados = {
#     123: 'Número inteiro',
#     (1, 2): 'Tupla',
#     'chave': 'String'
# }

# # Acessando valores com diferentes tipos de chave
# print(dados[123])     # Saída: Número inteiro
# print(dados[(1, 2)]) # Saída: Tupla
# print(dados['chave']) # Saída: String