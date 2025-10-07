palavras = ('Comunidade', 'Boliche', 'Analfabeto', 'Jenuario',
            'Golaço', 'Roliço', 'Agachamento', 'Jumento', 'Beliscar')
for rep in palavras:
    print(f'\nNa palavra {rep.upper()} temos', end=' ')
    for rep2 in rep:
        if rep2 in 'aeiou':
            print(f'{rep2}', end=' ')