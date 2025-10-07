preco = float(input('Digite o valor do produto: '))
print(f'Selecione o meio de pagamento: \n'
      f'[1] Pagamento em DINHEIRO/CHEQUE (10% de desconto)\n'
      f'[2] Pagamento á vista no cartão (5% de desconto)\n'
      f'[3] Pagemento em até 2x no cartão (Preço normal)\n'
      f'[4] Pagamento em até 3x ou mais no cartão (20% de JUROS totais)')
pagamento = int(input('Digite o meio de pagamento: '))

if pagamento == 1:
    dinheiro_cheque = preco - (preco * 0.10 )
    print(f'O valor final do seu produto é R${dinheiro_cheque:.2f}')

elif pagamento == 2:
        avista_desc = preco - (preco * 0.05)
        print(f'O valor final do seu produto é R${avista_desc:.2f}')

elif pagamento == 3:
        em_2x = preco / 2
        print(f'O valor final do seu produto é R${preco:.2f}\n'
              f'Você irá pagar R${em_2x} ao mês')

elif pagamento == 4:
    quantas_parcelas = int (input('Quantas parcelas? '))
    total = (preco * 0.20) + preco
    parcela = total / quantas_parcelas

    print(f'O valor final do seu produto é R${total:.2f}\n'
          f'Em {quantas_parcelas}x fica R${parcela:.2f} com JUROS')


else:
    print('Valor Inválido!\n'
          'Digite um dos valores acima!')
