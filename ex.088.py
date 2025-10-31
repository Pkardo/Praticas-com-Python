from random import randint #Busca a biblioteca de sortear números
print('-'*30)
print(f'{'Jogue na Mega Sena':^30}')
print('-'*30)
palpites = []
n = int(input('Quantos jogos você quer gerar? '))
for c in range(n): #Laço para mostrar a quatidade de listas sorteadas de acordo com oque o usuário digitou na variável (n)
    jogo = [] #cria uma nova lista
    while len(jogo) < 6: #laços para fazer a lista [jogo] receber apenas 6 números
        v = randint(1,61)
        if v not in jogo:
            jogo.append(v)
    palpites.append(jogo[:]) #adiciona a copia das listas [jogo]
print(f'-=-=  SORTEANDO {n} JOGOS  =-=-')
for i, v in enumerate(palpites): #laços para mostrar no print a posição e a lista no formato correto
    print(f'Jogo {i+1}: {v}')
print() #quebra a linha para ficar um em cima do outro
