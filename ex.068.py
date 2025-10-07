from random import randint
print('-='*13)
print('Vamos jogar PAR ou ÍMPAR')
print('-='*13)
resultado = ''
vitorias = 0
while True:
    escolha = str (input('Ímpar ou Par?[Impar/Par]: ')).upper().strip()
    if escolha == 'PAR' or escolha == 'IMPAR':
        num = int (input('Diga um valor: '))
        pc = randint(1,100) #escolha do pc
        soma = num + pc #soma par ou ímpar
        if soma % 2 == 0:
            resultado = 'PAR'
        else:
            resultado = 'IMPAR'
        if escolha == resultado:
            print(f'Você jogou ({num}) e o PC ({pc}). Total é {soma} {resultado}\n'
                  f'Tu GANHOU!\n'
                  f'Vamos jogar novamente..')
            vitorias += 1
            print('-=' * 15)
        else:
            print(f'Você jogou ({num}) e o PC ({pc}). Total é {soma} {resultado}\n'
                  f'Tu PERDEU BUXA!\n'
                  f'FIM DE JOGO! Você venceu {vitorias} vezes.')
            print('-=' * 15)
            break
    else:
        print('É ÍMPAR ou PAR burro')
