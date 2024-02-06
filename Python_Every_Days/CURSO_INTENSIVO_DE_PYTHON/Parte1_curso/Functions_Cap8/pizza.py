<<<<<<< HEAD
# Passando um numero arbitrario de argumentos
def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')
=======
def make_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
>>>>>>> bf08645 (day36 - classes)
