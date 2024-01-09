''' 
 18. Faça um programa que calcule a quantidade de 
 litros de combustível consumidos em uma viagem, 
 sabendo-se que o carro tem autonomia de 12 km por
 litro de combustível. 
 O programa deverá ler o tempo decorrido na viagem e a
 velocidade média e aplicar as fórmulas:

litrosDeCombustiveis
distanciaPercorrida

 D = (T * V)

 L = (D/12)

 
Em que:
• D = Distância percorrida em horas
• T = Tempo decorrido
• V = Velocidade média
• L = Litros de combustível consumidos
Ao final, o programa deverá imprimir a distância percorrida e a quantidade de
litros consumidos na viagem.
'''

tempoDecorrido = float(input("Qual o tempo decorrido:?"))
velocidadeMedia = float(input("Qual o tempo decorrido:?"))


distanciaPercorrida = (tempoDecorrido * velocidadeMedia)

litrosDeCombustiveis = (distanciaPercorrida/12)

print("o valor da distancia percorrida é de: ",distanciaPercorrida)
print("o valor de litros de combustiveis é de: ",litrosDeCombustiveis)