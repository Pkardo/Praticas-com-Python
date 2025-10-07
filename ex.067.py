'''num = 0
while True:
    print('_' * 35)
    num = int(input('Quer ver a tuabada de qual valor? '))
    if num < 0:
        print(f'Programa de tabuada encerrado!\n'
              f'Volte sempre!')
        break
    else:
        for resul in range(1,11):
            total = num * resul
            print(f'{num} x {resul} = {total}')'''

while True:
    print('_'*35)
    num = int(input('Quer ver a tuabada de qual valor(?): '))
    cont = 0
    if num < 1:
        print(f'Programa de tabuada encerrado!\n'
              f'Volte sempre!')
        break
    else:
        while cont < 10:
            cont += 1
            total = num * cont
            print(f'{num} x {cont} = {total}')

