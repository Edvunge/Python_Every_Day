def get_formatted_name(first_name, middle_name,last_name):
    """Devolve um nome completo formado de modo elegante."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)