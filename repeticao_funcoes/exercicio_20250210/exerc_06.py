
N = int(input('Digite o valor:  '))
i = 0
while i < N:
        i +=1
        if i == 1 or i == N:  
            e = 0
            while  e <= N: 
                print('*',end='')
                e+=1 
        else:
            e = 0
            while  e <= N: 
                if e <= N-1:
                    print(' ',end='') 
                else:
                    print('*',end='')  
                e+=1             
        print('')
