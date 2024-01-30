'''
14. Faça um programa que permita entrar com o salário 
de uma pessoa e imprima o
desconto do INSS segundo a tabela seguir:

Salário                                                 Faixa de Desconto
Menor ou igual à R$600,00                                       Isento
Maior que R$600,00 e menor ou igual a R$1200,00                 20%
Maior que R$1200,00 e menor ou igual a R$2000,00                25%
Maior que R$2000,00                                             30%
'''

salario = float(input("Digite o valor do salario:"))

if salario <= 600.00:
    print("esta isento do desconto do INSS.")
elif salario > 600.00 and salario < 1200.00:
    percentagem = (salario*20)/100
    salario = salario - percentagem
    print(f'o seu salario depois do desconto de 20% ficará R${salario}')
elif salario > 1200.00 and salario < 2000.00:
    percentagem = (salario*25)/100
    salario = salario - percentagem
    print(f'o seu salario depois do desconto de 25% ficará R${salario}')
elif salario > 2000.00:
    percentagem = (salario*30)/100
    salario = salario - percentagem
    print(f'o seu salario depois do desconto de 30% ficará R${salario}')
