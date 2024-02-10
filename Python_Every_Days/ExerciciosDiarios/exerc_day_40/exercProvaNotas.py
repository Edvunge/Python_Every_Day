""" 
Faça um programa em Python que leia as notas de 3 provas e calcule a média ponderada com pesos
respectivamente 1, 2 e 3 para as provas p1, p2 e p3.

Seu programa também deve escrever se o aluno está aprovado, reprovado ou em exame final, de acordo
com os intervalos abaixo:


• media ≥ 70: aprovado
• 40 ≤ media < 70: exame final
• media < 40: reprovado


Seu programa deve obrigatoriamente chamar uma
função chamada aprovado, que recebe as notas
das provas 1, 2 e 3, calcula a média ponderada (que
deve ser retornada como o valor de um parâmetro)
e retorna um inteiro com o valor:

• 1: se o aluno foi aprovado
• 0: se o aluno foi para exame
• -1: se o aluno foi reprovado

Por exemplo, a chamada de função aprovado( 90, 70, 60, media ) 
retorna o valor 0 e o valor de media 68.33.
Obs: A média ponderada é calculada da seguinte
forma:

"""

def aprovado(first_note, second_note, three_note):
    mediaPonderada = (((1 * first_note) + (2 * second_note) + (3 * three_note)) / 6)

    if mediaPonderada >= 70:
        return 1
    elif 40 <= mediaPonderada < 70:
        return 0
    else:
        return -1

# Leitura das notas
first_note = float(input("Digite a primeira nota: "))
second_note = float(input("Digite a segunda nota: "))
three_note = float(input("Digite a terceira nota: "))

# Chamada da função aprovado
resultado = aprovado(first_note, second_note, three_note)

# Impressão do resultado
if resultado == 1:
    print(f"Aprovado, média: {mediaPonderada}")
elif resultado == 0:
    print(f"Exame Final, média: {mediaPonderada}")
else:
    print(f"Reprovado, média: {mediaPonderada}")

