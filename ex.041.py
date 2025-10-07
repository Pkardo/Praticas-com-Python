from datetime import date
ano_nascimento = int (input('Digite seu ano de nascimento: '))
ano_atual = date.today().year

if ano_nascimento >= ano_atual:
    print('Ano de nascimento inválido!\n'
          'O ano não pode ser maior ou igual ao atual.')

idade = ano_atual - ano_nascimento

if ano_nascimento > 0 and ano_nascimento < ano_atual:

    if idade <= 9:
        print(f'O atleta tem {idade} anos.\n'
          f'Classificação: MIRIM')

    elif idade <= 14:
        print(f'O atleta tem {idade} anos.\n'
            f'Classificação: INFANTIL')

    elif idade <= 19:
        print(f'O atleta tem {idade} anos.\n'
                f'Classificação: JUNIOR')


    elif idade <= 25:
        print(f'O atleta tem {idade} anos.\n'
                f'Classificação: SÊNIOR')

    elif idade > 25:
        print(f'O atleta tem {idade} anos.\n'
                f'Classificação: MASTER')