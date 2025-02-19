par=[]
impar=[]
negativo=[]

def separar(valor):
    if valor % 2 == 0:
        par.append(valor)
    else:  
        impar.append(valor)
    if valor < 0:
        negativo.append(valor)

def separar(valor):     
    
def carregarlista(lista):
    for valor in lista:
        return valor
    

lista=[]
num=1
while num<=3:
   dado=int(input(f"Digite um numero {num}: "))
   lista.append(dado)
   num+=1
  
valortotal=0
for valor in lista:
    separar(valor)
    media(valor,sum(lista))


print(f'Numeros pares: {carregarlista(par)}')
print(f'Numeros impares: {carregarlista(impar)}')
print(f'Numeros negativos: {carregarlista(negativo)}')

   