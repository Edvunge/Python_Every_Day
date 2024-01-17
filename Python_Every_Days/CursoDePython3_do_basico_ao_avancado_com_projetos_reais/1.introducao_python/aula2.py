# aula 2 - python

'''
hoje falamos da função print.

Saída de dados com a função print
A função para imprimir dados em Python é a função print().

Ela é responsável por mostrar valores em seu terminal:


print('Olá Mundo')


-----------------------------------------------------------

O parâmetro sep= da função print
Por padrão, quando utilizamos virgula para separar os itens, a função print utiliza espaços para separar cada saída.

Porém, podemos utilizar o parâmetro sep= para definir um caractere de separação.

Entenda no exemplo a seguir:


    print('Dia', 'Mês', 'Ano', sep='/')
    print('ontem', 'Hoje', 'Amanhã', sep='-')
    print("B", "n", "n", ".", sep='a')

Observe a saída com os caracteres definidos:

    Dia/Mês/Ano
    ontem-Hoje-Amanhã
    Banana.



'''

# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

