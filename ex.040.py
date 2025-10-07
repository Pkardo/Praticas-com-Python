nota = float (input('Primeira nota: '))
nota2= float (input('Segunda nota: '))
media = (nota + nota2) / 2

if 0 <= nota <= 10 and 0 <= nota2 <= 10:

    if media < 5:
        print('O aluno está REPROVADO!')

    elif media >= 7:
        print('O aluno está APROVADO!')

    elif media >= 5 and media < 7:
        print(f'O aluno ficou de RECUPERAÇÃO!')

else:
    print(f'Invalido!')