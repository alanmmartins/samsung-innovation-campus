#o custo ao consumidor de um carro novo e a soma do preco de fabrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preco de fabrica .faca um programa em python que receba o preco de fabrica de um veiculo de o percentual de lucro do distribuidor e o percentual de imposto .calcule e mostre:
# a)o valor correspondente ao lucro do consumidor
# b)o valor correspondente aos impostos
# c)o preco final do veiculo 

# Solicita ao usuário que insira o preço de fábrica do veículo
preco_fabrica = float(input("Digite o preço de fábrica do veículo: "))

# Solicita ao usuário que insira o percentual de lucro do distribuidor
percentual_lucro = float(input("Digite o percentual de lucro do distribuidor (em %): "))

# Solicita ao usuário que insira o percentual de impostos
percentual_impostos = float(input("Digite o percentual de impostos (em %): "))

# Calcula o valor correspondente ao lucro
valor_lucro = preco_fabrica * (percentual_lucro / 100)

# Calcula o valor correspondente aos impostos
valor_impostos = preco_fabrica * (percentual_impostos / 100)

# Calcula o preço final do veículo
preco_final = preco_fabrica + valor_lucro + valor_impostos

# Exibe os resultados
print(f"Valor correspondente ao lucro do distribuidor: R${valor_lucro:.2f}")
print(f"Valor correspondente aos impostos: R${valor_impostos:.2f}")
print(f"Preço final do veículo: R${preco_final:.2f}")
