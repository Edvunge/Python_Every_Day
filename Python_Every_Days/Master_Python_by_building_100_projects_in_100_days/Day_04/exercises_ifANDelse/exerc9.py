'''
9. Faça um programa que permita entrar com o 
ano de nascimento da pessoa e como ano atual. 
O programa deve imprimir a idade da pessoa. 
Não se esqueça de verificar se o ano de nascimento informado é válido.
'''

ano_nascimento = int(input("Digite o seu ano nascimento:"))
ano_actual = int(input("digite o ano actual: "))

if ano_actual > ano_nascimento:
    idade = ano_actual - ano_nascimento
    print(f'a sua idade: {idade}anos.')
else: 
    print('impossivel calcular, valor invalido.')