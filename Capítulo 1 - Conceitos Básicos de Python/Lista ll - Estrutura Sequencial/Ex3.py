#sabe-se que:
# 1 pés = 12 polegadas
# 1 jarda = 3 Pés
# 1 milha = 1760 jardas
# faca um programa em python que receba uma medida em pés, faca as conversoes a seguir e mostre os resultados.
# a)polegadas
# b)jardas
# c)milhas

# Solicita ao usuário que insira a medida em pés
pes = float(input("Digite a medida em pés: "))

# Converte a medida para polegadas
polegadas = pes * 12

# Converte a medida para jardas
jardas = pes / 3

# Converte a medida para milhas
milhas = jardas / 1760

# Exibe os resultados
print(f"{pes} pés é igual a {polegadas} polegadas.")
print(f"{pes} pés é igual a {jardas} jardas.")
print(f"{pes} pés é igual a {milhas} milhas.")
