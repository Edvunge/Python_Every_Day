# 4. Faça um programa que leia um número e 
# informe se ele é ou não divisível por 5.

num = int(input("Digite um numero: "))

if num % 5 == 0:
    print(num," É divisivel por 5")
else: 
    print(num,"Não É divisivel por 5")