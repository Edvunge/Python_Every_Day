"""
Data com mês por extenso. 
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

def mesPorExtenso(dia, mes, ano):
    # Validação opcional da data
    if not (1 <= dia <= 31 and 1 <= mes <= 12):
        return None

    # Dicionários para mapear números para seus equivalentes em palavras
    meses_extenso = {
        1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril',
        5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
        9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'
    }

    # Construção da data por extenso
    data_extenso = f"{dia} de {meses_extenso[mes]} de {ano}"

    return data_extenso

# Exemplo de uso
data_por_extenso = mesPorExtenso(10, 2, 2024)

if data_por_extenso:
    print("Data por extenso:", data_por_extenso)
else:
    print("Data inválida!")
