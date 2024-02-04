# modificando uma lista em uma função

# Começa com alguns designs que devem ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simula a impressão de cada design, até que haja mais nenhum
# transfere cada design para completed_models apos a impressao
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # simula a criação de uma impressao 3d a partir do design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Exibe todos os modelos finalizados
print("\nThe folowing models have been printed:")
for completed_model in completed_models:
    print(completed_model)