
# 5. Escreva um programa que recebe do usuário um número A e um número B e então seu programa deve
# gerar um retângulo de asteríscos de tamanhos A e B conforme o exemplo abaixo:

A = int(input('Digite o valor de A:  '))
B = int(input('Digite o valor de B:  '))

i=0
vao = A - 2 # o vao em branco (subtrai duas casas do total de posições de A, 
            #                   ex: 8-2 = 6 de espaço/vao) 
while i < B:
        i +=1
        e=1 
        v=1
        if i == 1 or i == B:  
           while  e <= A: 
                print('*',end='')
                e += 1 
        else:
                print('*',end='') 
                while v <= vao:
                        print(' ',end='')
                        v+=1
                print('*',end='')
        
        print('')