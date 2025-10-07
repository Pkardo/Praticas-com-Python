salario = float (input('Digite o salário do funcionário: '))

salario_novo = (salario * 15 / 100) + salario
salario_novo2 = (salario *  10 / 100) + salario

if salario >= 1250:
    print(f'Quem ganhava R${salario} passa a ganhar R${salario_novo2:.2f}')

else:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario_novo:.2f}')