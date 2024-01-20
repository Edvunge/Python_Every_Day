""" 
3.7 - Reduzindo a lista de convidados: 
Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar 
e tem espaço para somente dois convidados.

• Comece com seu programa do Exercício 3.6. 
Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar 
apenas duas pessoas para o jantar.

• Utilize pop() para remover os convidados de sua lista, 
um de cada vez, até que apenas dois nomes permaneçam em sua lista. 
Sempre que remover um nome de sua lista, 
mostre uma mensagem a essa pessoa, permitindo que ela saiba que
você sente muito por não poder convidá-la para o jantar.

• Apresente uma mensagem para cada uma das duas pessoas que 
continuam na lista, 
permitindo que elas saibam que ainda estão convidadas.

• Utilize del para remover os dois últimos nomes de sua lista, 
de modo que você tenha uma lista vazia. 
Mostre sua lista para garantir que você realmente tem uma
lista vazia no final de seu programa.
"""
dinner_with_famous = ["Albert Einstein", "Linus Trovalds", "Ramiro Vunge"]

print(f'Os convidados: \n{dinner_with_famous[0]}, {dinner_with_famous[1]}, {dinner_with_famous[2]}, não estarão presentes.')

# Substituindo o convidado que não poderá comparecer
guest_not_attending = dinner_with_famous.pop(2)  # Removendo o terceiro convidado (índice 2)
new_guest = "Martin Luther King J."
dinner_with_famous.insert(0, new_guest)

print(f'\nInfelizmente, {guest_not_attending} não poderá comparecer ao jantar.')
print(f'Convidamos {new_guest} para participar do jantar.\n')

print("\nMalta posso convidar apenas duas pessoas.")

dinner_with_famous.insert(0, 'Pelé')
dinner_with_famous.insert(1, 'Malcon X')
dinner_with_famous.append('Pablo Neruda')

# Exibindo os convites atualizados
print("################ Lista de Convidados Atualizadas: ################")
print(f'Olá, amigão, vamos jantar: {dinner_with_famous[2]}')
print(f'Como analisa o desenvolvimento da ciência atual: {dinner_with_famous[0]}')
print(f'Como construir um legado igual ao teu: {dinner_with_famous[1]}')
