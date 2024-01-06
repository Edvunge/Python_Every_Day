'''
11. Faça um programa que leia dois números reais e 
calcule as quatro operações básicas entre 
estes dois números, adição, subtração, multiplicação e divisão. 
Ao final, o programa deve imprimir os resultados dos cálculos.
'''

num1 = float(input("Digite o primeiro numero real: "))
num2 = float(input("Digite o segundo numero real: "))

# soma:
soma = (num1 + num2)
print("O valor da soma e: ",soma)

# subtracao:
if num1 > num2:
    subtracao = (num1 + num2)
    print("O valor da subtracao e: ",subtracao)
else: 
    subtracao = (num2 + num1)
    print("O valor da subtracao e: ",subtracao)

# multiplicacao:
multiplicao = (num1 * num2)
print("O valor da multiplicacao e: ",multiplicao)


# divisao:
if num2 < 0: 
    num2 = float(input("Digite um outro numero real diferente de zero: "))
    divisao = (num1 + num2)
    print("O valor da divisao e: ",divisao)
else: 
    divisao = (num1 + num2)
    print("O valor da divisao e: ",divisao)
