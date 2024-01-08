# 15. Faça um programa que leia o valor de um produto, 
# o percentual do desconto desejado e imprima o 
# valor do desconto e o valor do produto subtraindo o desconto.

valorDoProduto = float(input("Valor do produto: "))
percentualDeDesconto = float(input("Digite o percentual de desconto: "))

valorDoProduto = (valorDoProduto * percentualDeDesconto/(100))

valorFinalDoProduto = (valorDoProduto - percentualDeDesconto)

print("O valor do produto: ", valorFinalDoProduto )
print("O valor do desconto: ", percentualDeDesconto)
