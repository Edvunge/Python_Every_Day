'''
13. Faça um programa que permita entrar com o nome, 
a nota da prova 1 e a nota da prova 2 de um aluno. 
O programa deve imprimir o nome, a nota da prova 1, a nota da prova 2, 
a média das notas e uma das mensagens: "Aprovado", "Reprovado"ou
"em Prova Final"(a média é 7 para aprovação, 
menor que 3 para reprovação e as demais em prova final).
'''

nome = input("Digite o seu nome: ")
notaPrimeiraProva = float(input("Digite a nota da prova 1"))
notaSegundaProva  = float(input("Digite a nota da prova 2"))

mediaDasNotas = ((notaPrimeiraProva+notaSegundaProva)/2)

if mediaDasNotas >= 7:
    print(f'o aluno {nome} Aprovado.')
elif mediaDasNotas < 3:
    print(f'o aluno {nome} Reprovado.')
elif mediaDasNotas <= 6 and mediaDasNotas >= 4:
    print(f'o aluno {nome} tera que refazer a prova final')