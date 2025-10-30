aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO!'
elif aluno['media'] < 5:
    aluno['situação'] = 'REPROVADO!'
else:
    aluno['situação'] = 'RECUPERAÇÃO!'
print('-='*20)
for i, a in aluno.items():
    print(f'{i} é igual a {a}')