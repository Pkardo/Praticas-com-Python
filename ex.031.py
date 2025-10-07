km = int (input('Qual a distância da sua viagem? '))

print(f'Sua viagem é de {km:.1f}Km!')

if km < 200:
    print(f'Sua passagem vai custar R${km * 0.50:.2f}')

if km >= 200:
    print(f'Sua passagem vai custar R$ {km * 0.45:.2f}')

