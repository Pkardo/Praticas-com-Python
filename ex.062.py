limit = 1
mais = 10
total = 0
cont = 0
print('Gerador de PA')
print('-='*7)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

while mais != 0:
        total += mais
        while limit <= total:
                print(termo, end=' ➡ ')
                limit = limit + 1
                termo += razao
                cont += 1
        print('Pausa')
        mais = int (input('Quantos termos você quer mais(?): '))
print(f'Você calculou exatamente {cont} termos')




