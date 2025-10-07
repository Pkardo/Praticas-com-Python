casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
pagamento_anos = float(input('Em quantos anos vai pagar? '))

parcelas_prestacao = casa / (12 * pagamento_anos)
salario_30 = salario * 0.30

if parcelas_prestacao <= salario_30:
    print(f'Para pagar uma casa de R${casa:.2f} em {pagamento_anos:.0f} anos a prestação será de R${parcelas_prestacao:.2f}\n'
          f'Empréstimo APROVADO!')
elif parcelas_prestacao > salario_30:
    print(f'Para pagar uma casa de R${casa:.2f} em {pagamento_anos:.0f} anos a prestação será de R${parcelas_prestacao:.2f}\n'
          f'Empréstimo NEGADO!')




