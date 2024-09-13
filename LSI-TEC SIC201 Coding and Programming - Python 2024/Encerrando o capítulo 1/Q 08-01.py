# Escreva um programa onde o usuário deve responder duas perguntas, se é maior de idade e se é casado, depois imprima o resultado.

# Exemplo:


# Você é maior de idade? (digite 1 se sim, 0 se não): 1
# Você é casado(a)? (digite 1 se sim, 0 se não): 0
# Você é maior de idade e solteiro.

# Solicita ao usuário se ele é maior de idade
maior_de_idade = int(input("Você é maior de idade? (digite 1 se sim, 0 se não): "))

# Solicita ao usuário se ele é casado
casado = int(input("Você é casado(a)? (digite 1 se sim, 0 se não): "))

# Verifica as respostas e imprime o resultado apropriado
if maior_de_idade == 1 and casado == 1:
    print("Você é maior de idade e casado(a).")
elif maior_de_idade == 1 and casado == 0:
    print("Você é maior de idade e solteiro(a).")
elif maior_de_idade == 0 and casado == 1:
    print("Você é menor de idade e casado(a).")
elif maior_de_idade == 0 and casado == 0:
    print("Você é menor de idade e solteiro(a).")
else:
    print("Entrada inválida. Por favor, digite 0 ou 1 para as respostas.")
