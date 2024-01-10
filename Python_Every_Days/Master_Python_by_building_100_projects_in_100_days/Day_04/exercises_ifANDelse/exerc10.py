'''
10. Faça um programa que leia três números inteiros 
e imprima os três em ordem crescente.
'''
num1 = int(input("digite o primeiro valor:"))
num2 = int(input("digite o segundo valor:"))
num3 = int(input("digite o terceiro valor:"))

if num1 > num2 and num1 > num3 and num3 > num2:
    print(f'1: {num2}') 
    print(f'2: {num3}')
    print(f'3: {num1}')
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f'1: {num1}') 
    print(f'2: {num3}')
    print(f'3: {num2}')
elif num3 > num2 and num3 > num1 and num1 > num2:
    print(f'1: {num2}') 
    print(f'2: {num1}')
    print(f'3: {num3}')
