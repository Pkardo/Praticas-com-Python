sexo = str(input('Digite seu genero [M/F]: ')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Digite novamente [M/F]: ')).upper().strip()
if sexo == 'M':
    print('Entendi, você é HOMEM!')
elif sexo == 'F':
    print('Entendi, você é MULHER!')