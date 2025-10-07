from datetime import date
nascimento = int (input('Qual seu ano de nascimento? '))
ano_atual = date.today().year
alistamento = ano_atual - nascimento

if alistamento == 18:
    print(f'Quem nasceu em {nascimento} tem {alistamento} ano(s) em {ano_atual}.\n'
          f'Você deve se alistar IMEDIATAMENTE!')
elif alistamento < 18:
    nao_18 = 18 - alistamento
    ano_alistamento = ano_atual + nao_18
    print(f'Quem nasceu em {nascimento} tem {alistamento} ano(s) em {ano_atual}.\n'
          f'Ainda faltam {nao_18} ano(s) para o alistamento!\n'
          f'Seu alistamento será em {ano_alistamento}')
elif alistamento > 18:
    mais_18 = alistamento - 18
    ano_alistamento = ano_atual - mais_18
    print(f'Quem nasceu em {nascimento} tem {alistamento} ano(s) em {ano_atual}.\n'
          f'Você já deveria ter se alistado há {mais_18} ano(s).\n'
          f'Seu alistamento foi em {ano_alistamento}.')
else:
    print(f'Digite um valor válido!')
