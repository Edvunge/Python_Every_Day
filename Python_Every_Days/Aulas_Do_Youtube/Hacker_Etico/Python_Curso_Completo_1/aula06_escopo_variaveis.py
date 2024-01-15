"""escopo de variaveis"""

'''
as variaveis globais

as variaveis locais
'''

x = 5

def funcao():
    x = 3
    print("valor da variavel local:",x)

funcao()
print("valor da variavel global:",x)
    