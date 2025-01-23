
# abre o arquivo exemplo.txt em modo leitura (r - read)
# a estrutura "with" lida automaticamente com o fechamento do arquivo 
with open('exemplo.txt', 'r') as arquivo:
    # le o arquivo, linha por linha
    for linha in arquivo:
        # mostra o conteudo da linha
        print(linha)

