alunos = []
while True:
    dados = []
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    duv = str(input('Quer continuar?[S/N]')).upper().strip()
    while duv not in 'SN':
        duv = str(input('Quer continuar?[S/N]')).upper().strip()
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    dados.append(media)
    alunos.append(dados)
    if duv == 'N':
        break
print('-='*30)
print(f'{'N°. NOME'} {'MÉDIA':^30}')
print(f'-'*30)
for i, v in enumerate(alunos):
    print(f'{i:<3} {v[0]:<15} {v[3]:^10}')
print('-'*40)
while True:
    mostrar = int(input('Mostrar Notas de qual aluno? (999 Interrompe): '))
    if mostrar == 999:
        break
    for v in range(len(alunos)):
        if mostrar == v:
            print(f'Notas de {alunos[v][0]} são {alunos[v][1]} e {alunos[v][2]}')
    print('-'*30)