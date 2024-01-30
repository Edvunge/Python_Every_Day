'''
17. Depois da liberação do governo para as mensalidades dos planos 
de saúde, as
pessoas começaram a fazer pesquisas para descobrir um bom plano, 
não muito caro. 
Um vendedor de um plano de saúde apresentou a tabela a seguir. 
Faça um programa que entre com o nome e a idade de uma pessoa e 
imprima o nome e o valor que ela deverá pagar.

Idade                                                   Valor
Até 10 anos                                             R$30,00
Acima de 10 até 29 anos                                 R$60,00
Acima de 29 até 45 anos                                 R$120,00
Acima de 45 até 59 anos                                 R$150,00
Acima de 59 até 65 anos                                 R$250,00
Maior que 65 anos                                       R$400,00
'''
nome = input("Digite o seu nome: ")
idade = int(input(f' {nome} digite a sua idade: '))

if idade < 10 :
    print(f'ola {nome}')
    print(f'a sua idade: {idade}anos.')
    print('o valor a pagar é de: R$30,00.')
elif idade < 10 and idade > 29:
    print(f'ola {nome}')
    print(f'a sua idade: {idade}anos.')
    print('o valor a pagar é de: R$60,00.')
elif idade < 29 and idade > 45:
    print(f'ola {nome}')
    print(f'a sua idade: {idade}anos.')
    print(f'o valor a pagar é de: R$120,00.')
elif idade < 45 and idade > 59:
    print(f'ola {nome}')
    print(f'a sua idade: {idade}anos.')
    print(f'o valor a pagar é de: R$150,00.')
elif idade < 59 and idade > 65:
    print(f'ola {nome}')
    print(f'a sua idade: {idade}anos.')
    print(f'o valor a pagar é de: R$250,00.')
elif idade > 65:
    print(f'ola {nome}')
    print(f'a sua idade: {idade}anos.')
    print(f'o valor a pagar é de: R$400,00.')