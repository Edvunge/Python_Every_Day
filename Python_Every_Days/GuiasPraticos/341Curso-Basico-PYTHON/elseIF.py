
"""
Restaurante do Zequinha
Manda quem pode, obedece quem tem juízo!
"""
pedido = input("O que deseja almoçar?\n")

if pedido == "arroz":
    print("Sim, senhor. Temos arroz, são R$ 5!")
elif pedido == "feijão":
    print("Sim, senhor. Temos feijão, R$ 10!")
elif pedido == "panquecas":
    print("As panquecas estão frias. São R$ 3 cada!")
else:
    print("Só temos arroz, feijão e panquecas!")