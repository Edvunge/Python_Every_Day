'''
12. Faça um programa que leia a idade de uma pessoa e informe:
• Se é maior de idade
• Se é menor de idade
• Se é maior de 65 anos
'''

idade = int(input("Digite a sua idade:"))

if idade > 18 and idade < 65:
    print("é maior de idade")
elif idade > 0 and idade < 18:
    print("é menor de idade")
elif idade >= 65:
    print("é maior de 65 anos")