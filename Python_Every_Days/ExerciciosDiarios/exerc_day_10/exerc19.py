'''
19. Em um campeonato nacional de arco-e-flecha, 
tem-se equipes de três jogadores para cada estado. 
Sabendo-se que os arqueiros de uma equipe não obtiveram o
mesmo número de pontos, 
criar um programa que informe se uma equipe
foi classificada, de acordo com a seguinte especificação:

• Ler os pontos obtidos por cada jogador da equipe;
• Mostrar esses valores em ordem decrescente;
• Se a soma dos pontos for maior do que 100,

imprimir a média aritmética entre eles, caso contrário, 
imprimir a mensagem "Equipe desclassificada".
'''

jogador_A = input("Digite o numero de pontos obtidos pelo jogador_A: ")
jogador_B = input("Digite o numero de pontos obtidos pelo jogador_B: ")
jogador_C = input("Digite o numero de pontos obtidos pelo jogador_C: ")


def ordemCrescente():
    if jogador_A > jogador_B and jogador_A > jogador_C or jogador_B > jogador_C:
        print(f'1. {jogador_A}, 2. {jogador_B}, 3. {jogador_C}')
    elif jogador_B > jogador_A and jogador_B > jogador_C or jogador_A > jogador_C:
        print(f'1. {jogador_B}, 2. {jogador_A}, 3. {jogador_C}')
    elif jogador_C > jogador_B and jogador_C > jogador_A or jogador_B > jogador_A:
        print(f'1. {jogador_A}, 2. {jogador_B}, 3. {jogador_C}')    

soma 
