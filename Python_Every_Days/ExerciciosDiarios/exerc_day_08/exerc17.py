''' 
17. Faça um programa que calcule a conversão entre graus centígrados e Fahrenheit.
Para isso, leia o valor em centígrados e calcule com base na fórmula a
seguir. Após calcular o programa deve imprimir o resultado da conversão.
Após calcular o programa deve imprimir o resultado da conversão.

Em que:

• F = Graus em Fahrenheit
• C = Graus centígrados
'''

grausCentigrados = float(input("Digite o valor dos grs. centigrados:"))

grausFahrenheit = (9 * grausCentigrados + 160)/5

print("O valor em graus fahrenheit: ",grausFahrenheit)