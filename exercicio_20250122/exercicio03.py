

with open("relatorio_usuario.txt",'r') as arquivo:
    for linha in arquivo:
          txt=linha.split('=')
          mb=int(txt[1].strip())/1048576
          print(f'Usuário: {txt[0]} ............. Uso do Disco ({round(mb)} MiB)')
