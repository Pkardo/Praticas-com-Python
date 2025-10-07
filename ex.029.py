from time import sleep

velocidade = int (input ('Qual a sua velocidade em Km/h atual? '))
multa = float (velocidade - 80) * 7 #multa estabelecida acima de 80km/h

print('Analisando sua velocidade...')
sleep(2)

if velocidade > 80:
    print(f'Você está acima do limite permitido!\n'
          f'Você será multado em R${multa:.2f}')
else:
    print('Você está dentro da velocidade permitida!')

