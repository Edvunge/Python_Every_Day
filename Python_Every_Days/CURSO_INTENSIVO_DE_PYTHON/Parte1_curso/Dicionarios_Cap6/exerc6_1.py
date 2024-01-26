''' 
6.1 – Pessoa: 
Use um dicionário para armazenar informações 
sobre uma pessoa que você conheça. 
Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. 
Você deverá ter chaves como first_name, last_name,
age e city. 
Mostre cada informação armazenada em seu dicionário.
'''

pessoa = {
    'first_name' : 'edvaldo',
    'last_name' : 'vunge',
    'age' : '28',
    'city' : 'lisboa',
}

print("Seu nome: " + pessoa['first_name'])
print("Seu ultimo nome: " + pessoa['last_name'])
print("A sua idade: " + pessoa['age'])
print("A sua cidade: " + pessoa['city'])