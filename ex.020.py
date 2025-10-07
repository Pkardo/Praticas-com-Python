import random
aluno1 = input ('Digite o nome do Grupo: ')
aluno2 = input ('Digite o nome do Grupo: ')
aluno3 = input ('Digite o nome do Grupo: ')
aluno4 = input ('Digite o nome do Grupo: ')

lista_grupos = [aluno1,aluno2,aluno3,aluno4]

print (f'A ordem de apresentação será:\n{random.sample(lista_grupos,k=4)}')
