'''
7. Faça um programa que leia um número e indique se o 
número está compreendido entre 20 e 50 ou não.
'''
num = int(input("digite um numero: "))

if num >= 20 and num <= 50:
    print(f'{num} esta no intervalo entre 20 e 50')
else:
    print(f'{num} não esta no intervalo entre 20 e 50')
