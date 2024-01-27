'''
Calcule a área de um círculo. 
Solicite ao usuário que insira o raio e exiba a área calculada.
'''

var_raio = float(input("digite o do raio:"))

# area = PI * raio ao quadrd
PI = 3.1415
area_do_circulo = (PI * (var_raio * var_raio))

print(f' a area do circulo: {area_do_circulo}')