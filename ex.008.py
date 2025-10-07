medida = float (input ('Uma distância em metros: '))
km = medida / 1000
hec = medida / 100
deca = medida / 10
deci = medida * 10
cent = medida * 100
mili = medida * 1000

print(f'A medida de {medida}m corresponde a \n' 
      f'{km:.3f}km\n'
      f'{hec:.2f}hm\n'
      f'{deca:.1f}dam\n'
      f'{deci:.0f}dm\n'
      f'{cent:.0f}cm\n'
      f'{mili:.0f}mm')


