# 16. Faça um programa que calcule o reajuste do salário de um 
# funcionário. Para isso, o programa deverá ler o salário atual 
# do funcionário e ler o percentual de reajuste. 
# Ao final imprimir o valor do novo salário.
 
salario = float(input("Qual o salario actual:?"))

percentagem = float(input("Qual o valor da percentagem:?"))

reajuste = (salario * 2/(100))

novoSalario = (salario + reajuste )

print("O valor do novo salario: ", novoSalario)