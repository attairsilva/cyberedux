


def entrada():
    con = 1
    valormaioranterior=0
    valormenoranterior=0
    soma = 0
    media = 0
    while con <= 3:
        valor = float(input(f'Valor nº {con}: '))
       
        if con==1:
           valormenoranterior=valor
            
        if valor > valormaioranterior:
            valormaioranterior=valor
        if valor < valormenoranterior:
            valormenoranterior=valor
        con += 1
        soma = soma + valor
      
    try:  
        media = soma /  con
    except:
        media = 'nao foi possivel'
    print(f'A soma deles é: {soma}')
    print(f'A media deles é: {valormaioranterior}')
    
    print(f'O maior numero é: { valormaioranterior}')
    print(f'O menor numero é: { valormenoranterior}')

entrada()
    
