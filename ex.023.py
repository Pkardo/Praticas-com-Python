'''num = int (input('Digite um numero de 0 a 9999: '))

if 0 <= num <= 9999:
    uni = str (num).zfill(4) [3]
    dez = str (num).zfill(4) [2]
    cen = str (num).zfill(4) [1]
    mil = str (num).zfill(4) [0]

    print(f'Analisando o número {num} \n'
      f'Unidade: {uni}\n'
      f'Dezena: {dez}\n'
      f'Centena: {cen}\n'
      f'Milhar: {mil}\n')'''

num = int (input('Digite um número de 0 a 9999: '))

if 0 <= num <= 9999:

    uni = (num // 1) % 10
    dez = (num // 10) % 10
    cen = (num // 100) % 10
    mil = (num // 1000) % 10

    print(f'Analisando o número.. \n'
          f'Unidade: {uni}\n'
          f'Dezena: {dez}\n'
          f'Centena: {cen}\n'
          f'Milhar: {mil}')

else:
    print('Error')

