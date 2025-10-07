#jogo de jokenpo
from random import randint
from time import sleep

print('Escolha sua jogada\n'
      '[0] - Pedra\n'
      '[1] - Papel\n'
      '[2] - Tesoura\n')

sua_jogada = int (input('Digite um valor: '))
jogada_pc = randint(0,2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!!')

if sua_jogada == 0 and jogada_pc == 1:
    print(f'Você escolheu PEDRA e o computador PAPEL.\n'
          f'Você PERDEU!')

elif sua_jogada == 0 and jogada_pc == 2:
    print('Você escolheu PEDRA e o computador TESOURA.\n'
          'BOAA, você VENCEU!')

elif sua_jogada == 0 and jogada_pc == 0:
    print('Você escolheu PEDRA e o computador PEDRA.\n'
          'EMPATOU, tente novamente!')

elif sua_jogada == 1 and jogada_pc == 0:
    print('Você escolheu PAPEL e o computador PEDRA.\n'
          'BOAA, você VENCEU!')

elif sua_jogada == 1 and jogada_pc == 2:
    print('Você escolheu PAPEL e o computador TESOURA.\n'
          'Você PERDEU!')

elif sua_jogada == 1 and jogada_pc == 1:
    print('Você escolheu PAPEL e o computador PAPEL.\n'
          'EMPATOU, tente novamente!')

elif sua_jogada == 2 and jogada_pc == 1:
    print('Você escolheu TESOURA e o computador PAPEL.\n'
          'BOAA, você VENCEU!')

elif sua_jogada == 2 and jogada_pc == 0:
    print('Você escolheu TESOURA e o computador PEDRA.\n'
          'Você PERDEU!!')

elif sua_jogada == 2 and jogada_pc == 2:
    print('Você escolheu TESOURA e o computador TESOURA.\n'
          'EMPATOU, tente novamente!')

else:
    print('Valor inválido!\n'
          'Digite um dos valores acima.')