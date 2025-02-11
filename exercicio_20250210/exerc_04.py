
numero = int(input('Infome um numero: '))
i=0
while i < numero:
    i+=1
    e=1
    b = numero-i # numero maximo de espaços de cada lado
    l=1
    
    #espaço do lado esquerdo
    while l <= b:
        print(' ',end='')
        l+=1
    
    #asteristico meio    
    while e <= i:
        print('*',end='')
        print(' ',end='')
        e+=1   
        
    print('')
