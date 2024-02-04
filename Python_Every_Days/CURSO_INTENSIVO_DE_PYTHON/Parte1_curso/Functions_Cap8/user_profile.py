# Usando argumentos nomeados arbitrarios
def build_profile(first, last, **user_info):
    """Constroi um dicionario contendo tudo que sabemos sobre um usuario."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location='princeton',
                             fields='physics')
print(user_profile)