# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

# lado = float(input("Digite o valor do lado: "))
valorPorHora = float(input("Digite o valor que ganha por hora: "))

horasTrabalhadsPorMes = int(input("Digite o numero de horas que trabalha no mes: "))

salario = (valorPorHora * horasTrabalhadsPorMes)

print ("O valor do seu salario: ", salario)
