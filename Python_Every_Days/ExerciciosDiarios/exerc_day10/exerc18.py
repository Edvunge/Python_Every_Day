'''
18. Faça um programa que leia um número inteiro entre 1 e 12 
e escreva o mês correspondente. 
Caso o usuário digite um número fora desse intervalo, deverá
aparecer uma mensagem informando que não existe mês com este número.
'''

numInt = input("digite um numero: ")

numInt = int(numInt)

if numInt == 1:
    print(f'{numInt} corresponde ao mes, Janeiro.')
elif numInt == 2:
    print(f'{numInt} corresponde ao mes, Fevereiro.')
elif numInt == 3:
    print(f'{numInt} corresponde ao mes, Março.')
elif numInt == 4:
    print(f'{numInt} corresponde ao mes, Abril.')
elif numInt == 5:
    print(f'{numInt} corresponde ao mes, Maio.')
elif numInt == 6:
    print(f'{numInt} corresponde ao mes, Junho.')
elif numInt == 7:
    print(f'{numInt} corresponde ao mes, Julho.')
elif numInt == 8:
    print(f'{numInt} corresponde ao mes, Agosto.')
elif numInt == 9:
    print(f'{numInt} corresponde ao mes, Setembro.')
elif numInt == 10:
    print(f'{numInt} corresponde ao mes, Outubro.')
elif numInt == 11:
    print(f'{numInt} corresponde ao mes, Novembro.')
elif numInt == 12:
    print(f'{numInt} corresponde ao mes, Dezembro.')
