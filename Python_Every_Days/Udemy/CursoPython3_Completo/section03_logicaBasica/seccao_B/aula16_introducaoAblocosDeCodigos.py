# if / elif     / else
# se / se nao se / se nao
entrada = input('Voce quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Voce entrou no sistema')
elif entrada == 'sair': 
    print('Voce saiu do sistema')
else:
    print('Voce não digitou entrar e nem sair')

print('FORA DOS BLOCOS')