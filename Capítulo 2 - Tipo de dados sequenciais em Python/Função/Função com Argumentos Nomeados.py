# Função com Argumentos Nomeados (Keyword Arguments)
def criar_usuario(nome, idade, email=None):
     usuario = {
         'nome': nome,
         'idade': idade,
         'email': email
}
     return usuario


print(criar_usuario('alan', 20))                 
print(criar_usuario('maria', 25, email='maria@.com'))  