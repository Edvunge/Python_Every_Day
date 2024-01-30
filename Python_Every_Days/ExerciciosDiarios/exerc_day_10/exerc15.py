'''
15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se
o valor da compra for menor que R$20,00, 
caso contrário, o lucro será de 30%.
Faça um programa que leia o valor do produto e imprima o valor da venda.
'''
valorCompra = float(input("Digite o valor da compra: "))
if valorCompra < 20.00:
    produto = (valorCompra * 45)/100
    valorDaVendaProduto = valorCompra + produto
    print(f'o valor da venda do produto: {valorDaVendaProduto}')
else:
    produto = (valorCompra * 30)/100
    valorDaVendaProduto = valorCompra + produto
    print(f'o valor da venda do produto: {valorDaVendaProduto}')
