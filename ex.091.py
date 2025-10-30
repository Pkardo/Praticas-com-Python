from operator import itemgetter
from random import randint
from time import sleep
print('Valores Sorteados:')
jogada = {'jogador1': randint(1,6),
          'jogador2': randint(1,6),
          'jogador3': randint(1,6),
          'jogador4': randint(1,6)}
ordem = []
for j, v in jogada.items():
    sleep(1)
    print(f'{j} tirou {v} em dado.')
print('-='*20)
ordem = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ordem):
    sleep(1)
    print(f' {i+1}° lugar: {v[0]} com {v[1]}.')