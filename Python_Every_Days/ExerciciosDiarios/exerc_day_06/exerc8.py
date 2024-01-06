# 8. Faça um programa que leia dois números inteiros 
# e imprima a subtração deles.

num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite um outro valor inteiro: "))

if num1 > num2:
    subtracao = num1 - num2
    print("o resultado da subtracao: ", subtracao)
else: 
    subtracao = num2 - num1
    print("o resultado da subtracao: ", subtracao)