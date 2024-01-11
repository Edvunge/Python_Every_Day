'''
16. A confederação brasileira de natação irá promover eliminatórias 
para o próximo mundial. 
Faça um programa que receba a idade de um nadador e imprima
a sua categoria segundo a tabela a seguir:

Categoria                       Idade
Infantil A                      5 - 7 anos
Infantil B                      8 - 10 anos
Juvenil A                       11 - 13 anos
Juvenil B                       14 - 17 anos
Sênior                          maiores de 18 anos
'''

idadeDoNadador = int(input("digite a idade do nadador: "))

if idadeDoNadador > 5 and idadeDoNadador < 7:
    print(f'a sua idade: {idadeDoNadador}anos voce é infantil A.')
elif idadeDoNadador > 8 and idadeDoNadador < 10:
    print(f'a sua idade: {idadeDoNadador}anos voce é infantil B.')
elif idadeDoNadador > 11 and idadeDoNadador < 13:
    print(f'a sua idade: {idadeDoNadador}anos voce é Juvenil A.')
elif idadeDoNadador > 14 and idadeDoNadador < 17:
    print(f'a sua idade: {idadeDoNadador}anos voce é Juvenil A.')
elif idadeDoNadador >= 18:
    print(f'a sua idade: {idadeDoNadador}anos voce é Senior.')