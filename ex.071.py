print('='*30)
print('          BANCO CEV          ')
print('='*30)
sobra = cedula_50 = cedula_20 = cedula_10 = cedula_1 = total_cedulas = 0
valor = int(input('Quanto você quer sacar(?): R$'))
cedula_50 = valor // 50
sobra = valor % 50
cedula_20 = sobra // 20
sobra = sobra % 20
cedula_10 = sobra // 10
sobra = sobra % 10
cedula_1 = sobra // 1
sobra = sobra % 1
if cedula_50 > 0:
    print(f'Total de {cedula_50} cédulas de R$50.')
if cedula_20 > 0:
    print(f'Total de {cedula_20} cédulas de R$20.')
if cedula_10 > 0:
    print(f'Total de {cedula_10} cédulas de R$10.')
if cedula_1 > 0:
    print(f'Total de {cedula_1} cédulas de R$1.')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')