'''
6. A prefeitura do Rio de Janeiro abriu uma linha de crédito 
para os funcionários estatutários. 
O valor máximo da prestação não poderá ultrapassar 30% do salário
bruto. 
Faça um programa que permita entrar com o salário bruto
e o valor da prestação e informar se o empréstimo 
pode ou não ser concedido.
'''


salario = input("Digite o valor do salario: ")
valorDaPrestacao = input("Digite a prestacao: ")

salario = float(salario)
valorDaPrestacao = float(valorDaPrestacao)

perc_30_Salario = (salario*30)/100

if valorDaPrestacao > perc_30_Salario:
    print("emprestimo concedido")
else:
    print("emprestimo não concedido")
