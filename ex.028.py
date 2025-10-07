from random import randint
from time import sleep

print('Eu pensei em um número entre 0 e 5. Tente adivinhar.. ')

num = int (input('Digite um número: '))

num_escolhido = randint(0,5)

print('Processando...')
sleep(2)

if num >= 0 and num <= 5: #inicio das condições

    if num == num_escolhido:
        print('Boaaa, você acertou, PARABÉNS!')

    else:
        print(f'Droga, você errou! \nO número que escolhi foi o {num_escolhido}, tente novamente.')

else:
    print('O valor digitado é inválido! Tente novamente.') #Fim das condições
