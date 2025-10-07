from random import choice
aluno1 = input ('Digite o nome do Aluno: ')
aluno2 = input ('Digite o nome do Aluno: ')
aluno3 = input ('Digite o nome do Aluno: ')
aluno4 = input ('Digite o nome do Aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

print (f'O aluno escolhido foi {choice(lista_alunos)}')