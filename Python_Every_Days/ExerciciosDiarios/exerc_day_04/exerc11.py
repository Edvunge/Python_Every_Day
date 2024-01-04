# Faça um Programa que peça 2 números inteiros e um número real. 
# Calcule  mostre:
#           o produto do dobro do primeiro com metade do segundo.
#           a soma do triplo do primeiro com o terceiro.
#           o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))


produto = ( (num1*num1) / num2 )
soma = ((num1*num1*num1)*num3)
num3 = (num3*num3*num3)


print ("o numero num3: ", num3)
print ("o valor da soma: ", soma)
print ("o valor do produto: ", produto)
