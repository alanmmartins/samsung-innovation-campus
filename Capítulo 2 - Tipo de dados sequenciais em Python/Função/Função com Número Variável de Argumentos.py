# Função com Número Variável de Argumentos

def imprimir_lista(*args):
     for item in args:
         print(item)


imprimir_lista(1, 2, 3)         # Saída: 1\n2\n3
imprimir_lista('a', 'b', 'c')   # Saída: a\nb\nc