'''cont = ('zero', 'um', 'dois', 'tres','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'desessete','dezoito', 'dezenove','vinte')
num = int (input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um valor: '))
print(f'Você digitou o número {cont[num]}')'''

cont = ('zero', 'um', 'dois', 'tres','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'desessete','dezoito', 'dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente.')
    else:
        if num >= 0 or num <= 20:
            print(f'Você digitou o número {cont[num]}')
            continuar = ' '
            while continuar not in 'SN':
                continuar = str(input('Você quer continuar(?)[S/N]: ')).upper().strip()
            if continuar == 'N':
                break
print('FIM DO PROGRAMA!')