# 13. Faça um programa que leia o saldo de uma conta 
# poupança e imprima o novo saldo, considerando umreajuste de 2%.

saldoDaConta = float(input("Qual o valor em conta:?"))

reajuste = (saldoDaConta * 2/(100))

novoSaldoDaConta = (saldoDaConta + reajuste )

print("O valor do reajuste e de: ", novoSaldoDaConta)