from time import sleep
from random import randint

'''print('Eu pensei em um número entre 0 e 5. Tente adivinhar..') #Forma de fazer 1
num_pc = int (randint(0,5)) #pc pensa em um número
num_jogador = int(input('Digite um número: '))
print('Processando..')
sleep(1) #espera 1 segundo

palpites = 0
while num_jogador != num_pc: #começa a repetição
    palpites += 1 #calcula quantas vezes errou
    print(f'Você ERROU! HAHAHA\n' #Mostra que errou
          f'O número que pensei foi {num_pc}')
    num_jogador = int(input('Tente novamente: ')) #pede para tentar novamente
    print('Processando..')
    sleep(1) #espera 1 segundo
    num_pc = int (randint(0,5)) #pc pensa em um número

print(f'Caramba, você ACERTOU!\n' #mostra que acertou
      f'O número que pensei foi {num_pc}\n'
      f'Você tentou {palpites} vezes até acertar.')'''


'''print('Eu pensei em um número entre 0 e 5. Tente adivinhar..') #Forma de fazer 2
num_pc = int (randint(0,10))
acertou = False
palpites = 0
while not acertou:
    num_jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if num_jogador == num_pc:
        acertou = True
    else:
        if num_jogador < num_pc:
            print('Mais..Tente mais uma vez.')
        elif num_jogador > num_pc:
            print('Menos..Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')'''


'''print('Eu pensei em um número entre 0 e 5. Tente adivinhar..') #Forma de fazer 3
num_pc = int (randint(0,10)) #pc pensa em um número
num_jogador = 0
palpites = 0
while num_jogador != num_pc: #começa a repetição
    palpites += 1 #calcula quantas vezes errou
    num_jogador = int(input('Digite sua tentativa: ')) #pede para tentar novamente
    if num_jogador < num_pc:
        print('Mais..tente novamente!')
    else:
        if num_jogador > num_pc:
            print('Menos..tente novamente!')

print(f'Caramba, você ACERTOU!\n' #mostra que acertou
      f'O número que pensei foi {num_pc}\n'
      f'Você tentou {palpites} vezes até acertar.')'''