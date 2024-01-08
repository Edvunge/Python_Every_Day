''' 
2. Faça um programa que leia dois valores inteiros e efetue a adição. 
Caso o valor somado seja maior que 20, 
este deverá ser apresentado somando-se a ele mais 8, 
caso o valor somado seja menor ou igual a 20, 
este deverá ser apresentado subtraindo-se 5.
'''

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

soma = num1 + num2

if soma > 20:
    print("valor: soma é ",soma+8)
elif soma <= 20: 
    print("valor: soma é ",soma-5)
