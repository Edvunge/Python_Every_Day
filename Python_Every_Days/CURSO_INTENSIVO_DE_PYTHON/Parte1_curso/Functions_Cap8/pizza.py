# Passando um numero arbitrario de argumentos
def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')