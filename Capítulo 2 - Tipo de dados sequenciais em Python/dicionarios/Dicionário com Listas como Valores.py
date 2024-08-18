#Dicionário com Listas como Valores

aluno = {
     'nome': 'João',
     'notas': [7.5, 8.0, 9.0],
     'disciplinas': ['Matemática', 'Português', 'História']
                     #0               1             2
      }
print (aluno)

# Acessando valores da lista
print(aluno['notas'])          # Saída: [7.5, 8.0, 9.0]
print(aluno['notas'][1])       # Saída: 8.0
print(aluno['disciplinas'][2]) # Saída: História