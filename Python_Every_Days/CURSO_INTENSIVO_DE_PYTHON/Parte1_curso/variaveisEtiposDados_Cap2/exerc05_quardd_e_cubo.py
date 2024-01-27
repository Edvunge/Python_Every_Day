'''
Desafio: Solicite ao usuário que insira um número inteiro. 
Depois, calcule e exiba o quadrado e o cubo desse número.
'''
var_numero = int(input("Digite um numero inteiro: "))

var_quadrdd = (var_numero * var_numero)
var_cubo = (var_numero * var_numero * var_numero)

print(f'o resultado do quadrado do {var_numero} eh de {var_quadrdd}')
print(f'o resultado do cubo do {var_numero} eh de {var_cubo}')