'''
21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
livro que será emprestado, o tipo de usuário (professor ou aluno) e possa imprimir
um recibo conforme mostrado a seguir. Considerar que o professor tem dez dias
para devolver o livro e o aluno só três dias.

• Nome do livro:
• Tipo de usuário:
• Total de dias:

p = 10
a = 3
'''

nomeDoLivro   = input("digite o nome do livro: ")
tipoDeUsuario = input("digite o tipo de usario\nProfesor(P) - Aluno(A)")


if tipoDeUsuario == 'P':
    totalDeDias = 10
    print(f'ola prof, o sr tem {totalDeDias}dias para entregar o livro: {nomeDoLivro}.')
else:
    totalDeDias = 3
    print(f'ola prof, o sr tem {totalDeDias}dias para entregar o livro: {nomeDoLivro}.')
