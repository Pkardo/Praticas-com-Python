cont = 0
cont2 = 0
from datetime import date
data_atual = date.today().year
for c in range(1,8):
    nasc = int ((input(f'Em que ano a {c}ª pessoa nasceu? ')))
    idade = data_atual - nasc

    if nasc > 0 and nasc <= data_atual:

        if idade >= 18:
            cont += 1

        elif idade < 18:
            cont2 += 1
    else:
        print('DIGITE UM ANO VÁLIDO!')


print(f'Ao todo tivemos {cont} pessoas maiores de idade\n'
      f'E também tivemos {cont2} pessoas menores de idade')

