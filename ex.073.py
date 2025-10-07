times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Mirassol', 'Botafogo', 'Bahia','São Paulo', 'Bragantino', 'Corinthians',
         'Fluminense', 'Ceará SC','Internacional','Atlético-MG','Grêmio','Vasco da Gama','Santos','EC Vitória','Juventude',
         'Fortaleza','Sport Recife')
print(f'Lista de times do Brasileirão: {times}')
print('=-'*20)
print(f'Os 5 primeiros são: {times[:5]}')
print('=-'*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-'*20)
print(f'Times em ordem Alfabética:{sorted(times)}')
print('=-'*20)
print(f'O São Paulo está na {times.index('São Paulo')} posição')