# Crie um programa que lei o arquivo ’emails.txt’ 
# e verifique se cada um dos emails tem um formato
# valido (siga o formato: xxxxxx@xxxx.xxx)
# Mostre no terminal o email caso ele seja inv´alido.
with open("lista_mails.txt",'r') as arquivo:
    texto = arquivo.read()
    for linha in texto.split('\n'):
          parte1=linha.split('@')
          if parte1[0]!='':
             parte2=parte1[0].split('.')
             if parte2[0]!= '':
                print(f'E-mail [{parte1[0]}] está incorreto')
          else:
             print(f'E-mail [{parte1[0]}]  [{parte1[1]}]está incorreto')
