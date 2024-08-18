# dicionario simples
# dados = {"nome" : "tercio" , "idade" : 27 , "cidade" : "sao paulo"   } 
# print (dados)

# Exemplo 1: Dicionário Simples


# Criando um dicionário
pessoa = {
    'nome': 'Alan',
    'idade': 25,     
    'cidade': 'São Paulo'
}

#  Acessando um valor pelo chave
print(pessoa['nome'])  # Saída: Alan
print(pessoa['idade']) # Saída: 25

#  Adicionando um novo par chave-valor
pessoa['email'] = 'alanmunozmartins@gmail.com'

#  Modificando um valor existente
pessoa['idade'] = 17 #saudadeskk

#  Removendo um par chave-valor
del pessoa['cidade']

print(pessoa)