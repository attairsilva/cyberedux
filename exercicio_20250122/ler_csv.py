def ler_arquivo(file):
    with open(file,'r') as f:
        texto = f.read()
    tabela=[] #cria uma lista
    
    for linha in texto.split('\n'): 
    #pega a linha ate a quebra
        if linha != '':
        #verifica linha vazia
            linha_tabela=[] 
            #cria nova lista de linha tabela
            for celula in linha.split(','):
            #separa o marcador na linha ','
                linha_tabela.append(celula)
                #inser o texto da linha na lista  
            tabela.append(linha_tabela) 
            #insere linha de tabela na lista tabela 
    for e in tabela:
      print(f'==> {e}')
ler_arquivo('lista_mails.csv')