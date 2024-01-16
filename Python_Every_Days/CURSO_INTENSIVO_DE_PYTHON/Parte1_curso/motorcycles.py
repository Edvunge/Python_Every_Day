# Modificando os Elementos de uma Lista

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Concatenando elementos no final de uma lista
motorcycles.append('ducati')
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


# Inserindo elementos em uma lista
motorcycles2 = ['honda','yamaha','suzuki']
motorcycles2.insert(0, 'ducati')
print(motorcycles2)

# Removendo Elementos de uma Lista

motorcycles3 = ['honda','yamaha','suzuki']
print(motorcycles3)

del motorcycles3[0]
print(motorcycles3)

# Removendo um item com o metodo pop()
motorcycles4 = ['honda','yamaha','suzuki']
print(motorcycles4)

popped_motorcycles = motorcycles4.pop()
print(motorcycles4)
print(popped_motorcycles)

# Removendo itens de qualquer posicao em uma lista

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


# Removendo um item de acordo com o valor 

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)