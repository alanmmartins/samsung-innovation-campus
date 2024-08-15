#faca um programa em python que receba o ano de nascimento de uma pessoa e o ano atual,calcule e mostre
# a)idade da pessoa
# b)quantos anos essa pessoa tera em 2055

# Solicita ao usuário que insira o ano de nascimento e o ano atual
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# Calcula a idade da pessoa
idade = ano_atual - ano_nascimento

# Calcula quantos anos a pessoa terá em 2055
ano_futuro = 2055
idade_em_2055 = idade + (ano_futuro - ano_atual)

# Exibe os resultados
print(f"A idade atual da pessoa é: {idade} anos.")
print(f"A pessoa terá {idade_em_2055} anos em 2055.")
