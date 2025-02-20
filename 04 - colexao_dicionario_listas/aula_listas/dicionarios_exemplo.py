meuprimeiro_dicionario={
    'marca':'Citrone',
    'modelo':'C4 Loung',
    'ano':'2018',
    'aibag':True,
    'acc':False,
    'mtor':[1.6,'turbo'],
    'automatico':[True,'Aisin TF-70SC'],
    'preço':145000.00  
}

meuprimeiro_dicionario['preço'] -= 100
meuprimeiro_dicionario['tipo']='sedã'

for chave, valor in meuprimeiro_dicionario.items():
    print(f'{chave} - {valor}')
