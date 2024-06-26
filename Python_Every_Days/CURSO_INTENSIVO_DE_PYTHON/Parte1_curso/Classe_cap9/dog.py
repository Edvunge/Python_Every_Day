class Dog():
    """Uma tentativa simples de modelar um cachorro."""

    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentado em resposta a um camndo."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simula um cachorro rolando em resposta a um camando."""
        print(self.name.title() + " rolled over!")