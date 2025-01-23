# abre o arquivo exemplo.txt em modo leitura (r - read)
arquivo = open('exemplo.txt', 'r')

# le o conteudo do arquivo
conteudo = arquivo.read()

# fecha o arquivo
arquivo.close()


# mostra o conteudo do arquivo
print(conteudo)
