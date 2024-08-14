# Faça um programa que preencha um vetor com os modelos de cinco carros
# (exemplos de modelos: Fusca, Gol, Vectra etc.). Carregue outro vetor com o
# consumo desses carros, isto é, quantos quilômetros cada um deles faz com um
# litro de combustível, calcule e mostre:
# • o modelo de carro mais econômico;
# • quantos litros de combustível cada um dos carros cadastrados
# consome para percorrer uma distância de 1.000 quilômetros.

# def main():
#     # Define a função principal do programa.

#     # Inicializando os vetores para armazenar os modelos e os consumos dos carros
#     modelos = []
#     # Cria uma lista vazia para armazenar os modelos dos carros.
    
#     consumos = []
#     # Cria uma lista vazia para armazenar o consumo (km/l) de cada carro.

#     # Coletando os modelos e os consumos dos carros
#     for i in range(5):
#         # Laço for que será executado 5 vezes, uma vez para cada carro.

#         modelo = input(f"Digite o modelo do carro {i+1}: ")
#         # Solicita ao usuário que digite o modelo do carro e armazena na variável 'modelo'.
        
#         modelos.append(modelo)
#         # Adiciona o modelo do carro na lista 'modelos'.
        
#         consumo = float(input(f"Digite o consumo do {modelo} (km por litro): "))
#         # Solicita ao usuário que digite o consumo do carro (km/l) e converte o valor para float.
        
#         consumos.append(consumo)
#         # Adiciona o consumo do carro na lista 'consumos'.

#     # Encontrando o carro mais econômico
#     max_consumo = max(consumos)
#     # Encontra o maior valor na lista 'consumos', que representa o consumo mais eficiente (mais km/l).
    
#     indice_mais_economico = consumos.index(max_consumo)
#     # Encontra o índice do carro mais econômico na lista 'consumos'.
    
#     modelo_mais_economico = modelos[indice_mais_economico]
#     # Usa o índice encontrado para obter o modelo do carro mais econômico na lista 'modelos'.

#     # Exibindo o modelo do carro mais econômico
#     print(f"\nO modelo mais econômico é o {modelo_mais_economico}, com um consumo de {max_consumo} km/l.")
#     # Exibe o modelo do carro mais econômico e seu consumo.

#     # Calculando e exibindo o consumo de combustível para 1.000 km
#     print("\nConsumo de combustível para percorrer 1.000 km:")
#     # Exibe um título para a lista de consumos de combustível.

#     for i in range(5):
#         # Laço for que será executado 5 vezes, uma vez para cada carro.

#         litros_necessarios = 1000 / consumos[i]
#         # Calcula quantos litros de combustível são necessários para percorrer 1.000 km.
        
#         print(f"{modelos[i]}: {litros_necessarios:.2f} litros")
#         # Exibe o modelo do carro e a quantidade de litros necessários, formatando o resultado com duas casas decimais.

# if __name__ == "__main__":
#     main()
    # Verifica se este arquivo está sendo executado diretamente (e não importado como módulo),
    # e, se for o caso, chama a função 'main' para iniciar o programa.

    #####################################################



def main():
    # Listas para armazenar os modelos dos carros e seus consumos
    modelos = []
    consumos = []

    # Solicitar ao usuário os dados dos carros
    for i in range(5):
        modelo = input(f"Digite o modelo do carro {i+1}: ")
        modelos.append(modelo)
        consumo = float(input(f"Digite o consumo do {modelo} (km por litro): "))
        consumos.append(consumo)

    # Encontrar o carro mais econômico
    mais_economico = consumos[0]
    modelo_mais_economico = modelos[0]

    for i in range(1, 5):
        if consumos[i] > mais_economico:
            mais_economico = consumos[i]
            modelo_mais_economico = modelos[i]

    # Exibir o modelo do carro mais econômico
    print(f"\nO modelo mais econômico é o {modelo_mais_economico}, com um consumo de {mais_economico} km/l.")

    # Calcular e exibir o consumo de combustível para 1.000 km para cada carro
    print("\nConsumo de combustível para percorrer 1.000 km:")
    for i in range(5):
        litros_necessarios = 1000 / consumos[i]
        print(f"{modelos[i]}:gasta {litros_necessarios:.2f} litros")

#O :.2f é uma forma de formatação usada em Python para formatar números de ponto flutuante (números decimais) e controlar como eles são exibidos. Vamos entender o que cada parte significa:

# :: Inicia a especificação do formato.
# .2f:
# .: Indica que você quer exibir um número decimal (ponto flutuante).
# 2: Define que você quer exibir exatamente duas casas decimais.
# f: Especifica que o valor é um número de ponto flutuante (ou seja, um número decimal).
# Exemplo:
# Se você tiver um número como 3.14159 e usar :.2f, ele será exibido como 3.14. Aqui, o número é arredondado para duas casas decimais.

if __name__ == "__main__":
    main()