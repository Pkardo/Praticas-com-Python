frase = str(input('Digite uma frase: ')).strip().upper()
corte = frase.split()
junto = ''.join(corte)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')

if junto == inverso:
    print(f'A frase digitada é um palíndromo!')

else:
    print('A frase digitada não é um palíndromo!')
