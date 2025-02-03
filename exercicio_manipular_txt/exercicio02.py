lista=[]

with open("lista_mails.txt",'r') as arquivo:
    for linha in arquivo:
      print(f'Gravando dado [{linha.strip()}] na LISTA')
      lista.append(linha.strip())

print('Exibindo LISTA')

for e in lista:
      print(f'E-mail: {e}')
      



    
     