#Dicionário com Tipos de Dados Variados


produto = {
     'id': 101,
     'nome': 'Laptop',
     'preço': 2999.99,
     'disponível': True,
     'especificações': {
         'processador': 'Intel i7',
         'ram': '16GB',
         'armazenamento': '512GB SSD'
    }
}
print (produto)

 # Acessando um valor em um dicionário aninhado
print(produto['especificações']['processador'])  # Saída: Intel i7
