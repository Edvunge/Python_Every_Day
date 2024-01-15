''' 
3 - se o produto que voce quer avaliar custa
(??) reais qual será o valor do mesmo com desconto de (??)%.
'''
produto = float(input("Digite o valor do produto: "))
desconto = int(input("Digite o valor do desconto: "))

desconto = (produto * desconto)/100
valor_final_prod = produto - desconto

print(f'O valor final do produto eh de: {valor_final_prod}')
