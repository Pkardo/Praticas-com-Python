from datetime import date
aposen = dict()
aposen['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
aposen['idade'] = date.today().year - ano_nasc
aposen['sexo'] = str(input('Qual o seu gênero?[M/F]: ')).upper().strip()
while aposen['sexo'] not in 'MF':
    aposen['sexo'] = str(input('Qual o seu gênero?[M/F]: ')).upper().strip()
aposen['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if aposen['ctps'] != 0:
    aposen['contratação'] = int(input('Ano de contrato: '))
    aposen['salario'] = float(input('Salário R$:'))
    if aposen['sexo'] == 'M':
        aposen['aposentadoria'] = (aposen['contratação'] - ano_nasc) + 35
    elif aposen['sexo'] == 'F':
        aposen['aposentadoria'] = (aposen['contratação'] - ano_nasc) + 30
print('-='*30)
for n, v in aposen.items():
    print(f'- {n} tem o valor {v}')