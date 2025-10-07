print('Analise de IMC')
peso = float(input('Digite seu peso? (Kg): '))
altura = float(input('Digite sua altura? (m): '))

total_imc = peso / (altura ** 2)

if total_imc <= 18.5:
    (print(f'Seu IMC é de {total_imc:.1f}\n'
           f'Você está ABAIXO do peso normal!'))
elif total_imc <= 25:
    print(f'O seu IMC é de {total_imc:.1f}\n'
          f'Você está no seu peso IDEAL!')
elif total_imc <= 30:
    print(f'O seu IMC é de {total_imc:.1f}\n'
          f'Cuidado, você está com SOBREPESO!')
elif total_imc <= 40:
    print(f'O seu IMC é de {total_imc:.1f}\n'
          f'Se cuide, você já está OBESO!')
else:
    print(f'O seu IMC é de {total_imc:.1f}\n'
          f'Se cuide urgentemente, você está com OBESIDADE MORBIDA!')