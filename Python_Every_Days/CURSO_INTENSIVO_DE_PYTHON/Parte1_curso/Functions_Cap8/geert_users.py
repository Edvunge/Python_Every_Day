# passando uma lista por parametro
def geert_users(names):
    """Exibe uma saudação simples a cada usuario da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
geert_users(usernames)