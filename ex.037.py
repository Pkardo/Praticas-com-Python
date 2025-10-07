from random import randint

num = int (input('Digite um número: '))

binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]

print('Escolha uma das bases para conversão: \n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL\n')

escolha = int (input('Digite um valor: '))

if escolha == 1:
      print(f'{num} convertido para BINÁRIO é igual a {binario}')

elif escolha == 2:
      print(f'{num} convertido para OCTAL é igual a {octal}')

elif escolha == 3:
      print(f'{num} convertido para HEXADECIMAL é igual a {hexadecimal}')

else:
      print('Valor invalido!\n')