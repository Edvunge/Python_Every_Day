'''
def greet_user():
    """Exibe uma saudacao simples."""
    print("Hello!")
'''
# passando informações para uma função

def greet_user(username):
    """ Exibe uma saudação simples."""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')
