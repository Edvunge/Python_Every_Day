# faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor

number = int(input('Digite um numero inteiro: '))

sucessor = number + 1
print("O Sucessor do {} e {} ".format(number, sucessor))

antecessor = number - 1
print("O Antecessor do {} e {} ".format(number, antecessor))