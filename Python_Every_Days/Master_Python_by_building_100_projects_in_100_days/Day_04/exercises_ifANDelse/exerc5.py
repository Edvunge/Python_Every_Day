# 5. Faça um programa que leia um número e informe 
# se ele é divisível por 3 e por 7.

num = int(input("Digite um numero: "))

if num % 3 == 0  and  num % 7 == 0:
    print(num," É divisivel por 3 e 7")
else: 
    print(num,"Não É divisivel por 3 e 7")