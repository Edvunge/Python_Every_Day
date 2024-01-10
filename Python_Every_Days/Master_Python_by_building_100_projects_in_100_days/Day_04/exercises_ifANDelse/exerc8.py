'''
8. Faça um programa que leia um número e imprima uma das mensagens: 
"Maior do que 20", "Igual a 20"ou "Menor do que 20".
'''
num = int(input("digite um numero inteiro: "))

if num > 20:
    print(f'{num} maior que 20')
elif num == 20:
    print(f'{num} igual que 20')
else:
    print(f'{num} menor que 20')