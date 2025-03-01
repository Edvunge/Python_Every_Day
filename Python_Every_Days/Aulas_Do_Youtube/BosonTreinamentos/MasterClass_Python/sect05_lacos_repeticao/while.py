# num = 1

# while (num <= 10):
#    print(num)
#    num += 1
#print('Laço encerrado!')

nome = None

while True:
    print('Digite seu nome, ou X para parar:')
    nome = input()
    if nome == 'X' or nome == 'x':
        break
    print(f'Bem-vindo, {nome}')
print('ate logo')