'''
11. Faça um programa que leia 3 números e imprima o maior deles.
'''

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
num3 = int(input("Digite o terceiro valor:"))

if num1 > num2 and num1 > num3:
    print(f'O maior valor é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior valor é {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior valor é {num3}')