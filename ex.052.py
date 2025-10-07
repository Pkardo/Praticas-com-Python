cont = 0
cont2 = 0
num = int (input('Digite um número: '))

for c in range(1, num+1):

    if num % c == 0:
        cont += 1
        print(f'\033[32m{c}', end=' ')

    else:
        print(f'\033[31m{c}', end=' ')

if cont == 2:
    print(f'\n\033[33mO número {num} foi divisível {cont} vezes\n'
          f'E por isso ele é PRIMO!')

else:
    print(f'\n\033[33mO número {num} foi divisível {cont} vezes\n'
          f'Por isso ele NÃO É PRIMO!')