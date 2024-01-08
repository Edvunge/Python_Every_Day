''' 
3. Faça um programa que leia um número e imprima uma das duas mensagens: "É
múltiplo de 3"ou "Não é múltiplo de 3".
'''

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

soma = num1 + num2

if soma > 20:
    print("valor: soma é ",soma+8)
elif soma <= 20: 
    print("valor: soma é ",soma-5)
