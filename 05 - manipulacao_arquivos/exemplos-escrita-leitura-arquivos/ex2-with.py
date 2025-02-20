# abre o arquivo exemplo.txt em modo leitura (r - read)
# a estrutura "with" lida automaticamente com o fechamento do arquivo 
with open('exemplo.txt', 'r') as arquivo:
    # le o conteudo do arquivo
    conteudo = arquivo.read()

# mostra o conteudo do arquivo
print(conteudo)

