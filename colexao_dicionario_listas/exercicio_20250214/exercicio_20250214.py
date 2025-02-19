# Escreva um programa que recebe do usuário as seguintes informações:
# Nome do aluno, Notas do aluno (3 notas)
# O programa deve permitir receber essas informações quantas vezes o usuário quiser. 
# O seu programa deve armazenar essas informações em 4 coleções de dados diferentes
# As coleções devem ter os seguintes formatos:

colecaoA=[]
colecaoB=[]
colecaoC={}
colecaoD=[]

def addColecaoA(lista,nome):
    colecaoA.append(nome)
    for valor in lista:
        colecaoA.append(valor)
    return colecaoA

# Coleção A
# [
#  "nome do aluno", nota_1, nota_2, nota_3,
#  "nome do aluno2", nota_1, nota_2, nota_3,
#  ...
# ]
# Col      

def addColecaoB(lista,nome):
    tupla = (nome,lista)
    colecaoB.append( tupla)
    return colecaoB

# Coleção B
# [
#  ("nome do aluno", [nota_1, nota_2, nota_3]),
#  ("nome do aluno2", [nota_1, nota_2, nota_3]),
#  ...
# ]

def addColecaoC(lista,nome):  
    colecaoC[nome]=lista
    return colecaoC

# Coleção C
# {
#  "nome do aluno": [nota_1, nota_2, nota_3],
#  "nome do aluno2": [nota_1, nota_2, nota_3],
#  ...
# }

def addColecaoD(lista,nome): 
    nomenotaDic = {}
    nomenotaDic['nome'] = nome
    nomenotaDic['notas'] = lista
    colecaoD.append(nomenotaDic)
    return colecaoD

# Coleção D
# [
#  { "nome": "nome do aluno", "notas": [nota_1, nota_2, nota_3]},
#  { "nome": "nome do aluno2", "notas": [nota_1, nota_2, nota_3]},
#  ...
# ]

while True:
   nome=input(f"Digite o nome do aluno: ")
   num=1
   notas=[]
   if nome =='':
       break
   while num<=3:
    nota=float(input(f"Digite a nota {num}: "))
    notas.append(nota)
    num+=1
   
   colecaoA=addColecaoA(notas,nome)
   colecaoB=addColecaoB(notas,nome)
   colecaoC=addColecaoC(notas,nome)
   colecaoD=addColecaoD(notas,nome)
   


# Ao final da inserção dos dados o programa deve:
# mostrar todas as coleções que foram criadas
# mostrar os dados contidos em todas coleções, ou seja, 
# percorrer a coleção e mostrar o nome e notas
# de cada aluno


print ('=================================')
print ('Coleção A: ')
print ('=================================')
cta=0
r=0
for nomeNota in colecaoA:
    cta+=1
    if cta==1:
        nome = nomeNota
        print(f"** Nome: {nome}") 
    else:
        if cta>1 or cta<=4:
            print(f"    - Nota: {nomeNota}")  
        if cta == 4:
            cta=0
    

print ('=================================')
print ('Coleção B: ')
print ('=================================')
for nome,nota in colecaoB:
    print(f"** Nome {nome}:")
    cta=0
    for valor in nota: 
        cta+=1
        print(f" Nota {cta} = {valor}")
        
print ('=================================')  
print ('Coleção C: ')
print ('=================================')
for chave, notas in colecaoC.items():
        print(f'** Nome: {chave}')
        for valor in notas:
            print(f'- Nota: {valor}')

print ('=================================')
print ('Coleção D: ')
print ('=================================')
for nome in colecaoD:   
    print(f"** Nome: {nome["nome"]}:") 
    carreganotas = nome["notas"]
    for valor in carreganotas:
            print(f'- Nota: {valor}')
        