nome = 'edvaldo'

# print(nome[2])
print('v' in nome)
print('zero' in nome)
print(10 * '-')
print('v' not in nome)
print('zero' not in nome)
print(10 * '-')

encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:    
    print(f'{encontrar} não está em {nome}')
