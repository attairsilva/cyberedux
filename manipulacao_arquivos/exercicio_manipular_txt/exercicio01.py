lista=[]
dado=input("Digite um e-mail: ")
while dado!='':
   lista.append(dado)
   dado=input("Digite um e-mail: ")
   

with open("lista_mails.txt",'w') as arquivo:
  for e in lista:
      print(f'Gravando email {e} no Arquivo')
      arquivo.write(e + '\n')



    
     