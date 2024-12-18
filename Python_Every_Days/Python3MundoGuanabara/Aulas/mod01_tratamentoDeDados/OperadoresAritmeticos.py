# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
potencia = n1 ** n2
print('A soma é {}, o produto é {} e a divisao é {}'.format(soma, multiplicacao, divisao))
print('Divisao inteira {} e a potencia {}'.format(divisao_inteira, potencia))