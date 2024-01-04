# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

   alturaH = float(input("Digite a altura: "))
sexo = input("Digite o sexo (H para homem, M para mulher): ")

if sexo.upper() == 'H':
    pesoIdeal = (72.7 * alturaH) - 58
    print("Peso ideal do homem é:", pesoIdeal)
elif sexo.upper() == 'M':
    pesoIdeal = (62.1 * alturaH) - 44.7
    print("Peso ideal da mulher é:", pesoIdeal)
else:
    print("Opção de sexo inválida. Use 'H' para homem ou 'M' para mulher.")
