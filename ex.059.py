from time import sleep
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))

num3 = 0
while num3 != 5:
    print('=-=' * 10)
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Adicionar novos números\n'
          '[5] Sair do programa')
    num3 = int(input('>>>> Digite um valor: '))

    if num3 == 1:
        print(f'A SOMA entre {num1} e {num2} é igual a {num1+num2}')


    elif num3 == 2:
        print(f'A MULTIPLICAÇÃO entre {num1} e {num2} é igual a {num1*num2}')


    elif num3 == 3:
        if num1 > num2:
            print(f'O MAIOR entre os dois valores digitados é {num1}')
        else:
            print(f'O MAIOR entre os dois valores digitados é {num2}')

    elif num3 == 4:
            num1 = int(input('Digite um novo valor: '))
            num2 = int(input('Digite um novo valor: '))

    elif num3 == 5:
        print(f'Finalizando..')
        sleep(1)
        print(f'Fim do programa. Volte sempre!')

    else:
        print('>>>> Opção inválida. Tente novamente! <<<<')

    sleep(2)
