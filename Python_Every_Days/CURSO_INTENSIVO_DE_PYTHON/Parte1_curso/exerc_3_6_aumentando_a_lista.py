"""
3.6 - Mais convidados: 
Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. 
Pense em mais três convidados para o jantar.

• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. 
Acrescente
uma instrução print no final de seu programa 
informando às pessoas que você
encontrou uma mesa de jantar maior.

• Utilize insert() para adicionar um novo convidado 
no início de sua lista.

• Utilize insert() para adicionar um novo convidado 
no meio de sua lista.

• Utilize append() para adicionar um novo convidado 
no final de sua lista.

• Exiba um novo conjunto de mensagens de convite, 
uma para cada pessoa que está em sua lista.
"""

dinner_with_famous = ["Albert Einstein", "Linus Trovalds", "Ramiro Vunge"]

print(f'Os convidados: \n{dinner_with_famous[0]}, {dinner_with_famous[1]}, {dinner_with_famous[2]}, não estarão presentes.')

# Substituindo o convidado que não poderá comparecer
guest_not_attending = dinner_with_famous.pop(2)  # Removendo o terceiro convidado (índice 2)
new_guest = "Martin Luther King J."
dinner_with_famous.insert(0, new_guest)

print(f'\nInfelizmente, {guest_not_attending} não poderá comparecer ao jantar.')
print(f'Convidamos {new_guest} para participar do jantar.\n')

print("\nMalta encontrei uma mesa maior, teremos novos convidados.")

dinner_with_famous.insert(0, 'Pelé')
dinner_with_famous.insert(1, 'Malcon X')
dinner_with_famous.append('Pablo Neruda')

# Exibindo os convites atualizados
print("################ Lista de Convidados Atualizadas: ################")
print(f'Olá, amigão, vamos jantar: {dinner_with_famous[2]}')
print(f'Como analisa o desenvolvimento da ciência atual: {dinner_with_famous[0]}')
print(f'Como construir um legado igual ao teu: {dinner_with_famous[1]}')
