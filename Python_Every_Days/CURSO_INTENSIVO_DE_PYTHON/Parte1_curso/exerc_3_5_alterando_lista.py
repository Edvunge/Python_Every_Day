"""
3.5 - Alterando a lista de convidados: 
Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, 
portanto será necessário enviar um
novo conjunto de convites. 
Você deverá pensar em outra pessoa para convidar.

• Comece com seu programa do Exercício 3.4. 
Acrescente uma instrução print
no final de seu programa, 
especificando o nome do convidado que não poderá
comparecer.

• Modifique sua lista, 
substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.

• Exiba um segundo conjunto de mensagens com o convite, 
uma para cada
pessoa que continua presente em sua lista.
"""

dinner_with_famous = ["Albert Einstein", "Linus Trovalds", "Ramiro Vunge"]

print(f'Os convidados: \n{dinner_with_famous[0]}, {dinner_with_famous[1]}, {dinner_with_famous[2]}, não estarão presentes.')

# Substituindo o convidado que não poderá comparecer
guest_not_attending = dinner_with_famous.pop(2)  # Removendo o terceiro convidado (índice 2)
new_guest = "Martin Luther King J."
dinner_with_famous.insert(0, new_guest)

print(f'\nInfelizmente, {guest_not_attending} não poderá comparecer ao jantar.')
print(f'Convidamos {new_guest} para participar do jantar.\n')

# Exibindo os convites atualizados
print("################ Lista de Convidados Atualizadas: ################")
print(f'Olá, amigão, vamos jantar: {dinner_with_famous[2]}')
print(f'Como analisa o desenvolvimento da ciência atual: {dinner_with_famous[0]}')
print(f'Como construir um legado igual ao teu: {dinner_with_famous[1]}')
