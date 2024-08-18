# Dicionário com Chaves de Tipos Diferentes


dados = {
     123: 'Número inteiro',
     (1, 2): 'Tupla',
     'chave': 'String'
}


print(dados[123])     # Saída: Número inteiro
print(dados[(1, 2)]) # Saída: Tupla
print(dados['chave']) # Saída: String