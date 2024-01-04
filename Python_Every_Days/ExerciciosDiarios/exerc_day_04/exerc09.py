# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

grausFahrenheit = float(input("Digite o valor em graus Fahrenheit: "))

grausCelsius = 5 * ( (grausFahrenheit - 32) / 9 )

print ("o valor em gaus celsius: ", grausCelsius)
