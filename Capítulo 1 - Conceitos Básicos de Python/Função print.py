#Para imprimir uma string usando a função print( ), você deve colocar a cadeia entres aspas.
print('Hello World')
print("Hello World")

#Para imprimir um valor numérico usando a função print(),digite os números sem aspas. Se um número entre aspas for colocado na função print(), o tipo de dado será um número inteiro
print(10)
print(7.5)

#Você também pode realizar operações aritméticas com a função print( ).
print(10 + 7.5)
print(10 - 7.5)

#Adicionando uma nova linha
#Python quebra automaticamente a linha após imprimir uma string por meio da função print( ). Em caso afirmativo, as linhas poderiam quebrar entre frases dentro da mesma função print( )?
#O uso de "\n" acrescenta uma nova linha.
print('Hello\nWorld!')

#Adicionando uma nova linha
#Na função print( ), o início e o fim de uma cadeia podem ser agrupados com três aspas duplas (""") ou três aspas simples ('''). Isto exibirá a cadeia agrupada, incluindo a quebra de linha, na tela. 
print('''Hello
      
World!''')

#Entretanto, se você colocar uma contrabarra (＼) no final de uma string agrupado com três aspas, a linha não será quebrada, e a próxima linha será conectada à mesma linha.
print('''Hello\
World!''')

#A Vírgula(,) Adições(+), Multiplicação(*) Operadores
#Uma vírgula, adição ou operadores de multiplicação podem ser usados para imprimir strings ou valores mais diversificados e eficientes.
#Quando um operador com vírgula (,) é usado entre o primeiro e o segundo valor, ele adiciona um espaço entre os valores e depois uma quebra de linha. Você pode imprimir dois ou mais números inteiros ou valores combinando-os com um operador de vírgula. 
print('Hello', 'World!')
print(10,20)

#Você também pode combinar uma string e um número com um operador de vírgula. 
print('Hello', 10)

#Quando strings são combinadas com um operador de adição (+), o segundo inteiro é impresso após o primeiro inteiro sem um espaço, então ocorre uma quebra de linha. Quando um operador de adição (+) é usado com valores, ele imprimirá o resultado da adição, então ocorre uma quebra de linha
print('Hello' + 'World!')
print(10 + 20)
###Ao utilizar um operador de adição (+), não é possível combinar strings e números. Quando uma string e um número são combinados com um operador de adição (+), ocorre o TypeError. ###print('Hello' + 10)###

#Quando uma string e um inteiro positivo são combinados usando um operador de multiplicação (*), a string é repetida tantas vezes quanto o número e sem nenhum espaço, então ocorre uma quebra de linha. Quando um operador de multiplicação (*) é usado para um número, ocorre uma quebra de linha após a impressão do resultado da operação de multiplicação.
print('Hello' * 3)
print(10 * 20)
###Quando duas strings são combinadas com um operador de multiplicação (*), ocorre o TypeError.###print('Hello' * 'World')###

#Parâmetros End e Split
#Quando um programa encontra uma função print(), ocorre uma quebra de linha. Entretanto, quando uma string é especificada no final da declaração print( ), a string é impressa em vez da quebra de linha.
#O primeiro código imprime "Olá" e depois imprime imediatamente "Mundo!" sem quebrar a linha. O segundo código imprime uma vírgula ao invés de uma quebra de linha.
print('Hello', end = ' ')
print('World!')

print('Hello', end = ',')
print('World!')

#Parâmetros de End e Split

#A vírgula (,) anteriormente apresentada dentro da função print() imprime um espaço entre duas string ou valores. Quando uma string é especificada e por último se coloca um "sep" da função print( ), a string especificada é impressa ao invés do espaço.
#O primeiro código imprime "Hello" e depois imprime imediatamente "World!" sem espaços. O segundo código imprime uma vírgula ao invés de um espaço.
print('Hello', 'World!', sep = ' ')

print('Hello', 'World!', sep = ',')

#Apresentação do código 

#Python permite escrever várias frases em uma linha usando ponto-e-vírgula, como mostrado abaixo. Este estilo de codificação, no entanto, não tem uma boa legibilidade.
a= 10; a+=10; print(a) #Implementação ruim


#Ao codificar com Python, é recomendável usar uma frase em cada linha, como mostrado abaixo.
a= 10 #Boa implementaçãoa+=10print(a)




