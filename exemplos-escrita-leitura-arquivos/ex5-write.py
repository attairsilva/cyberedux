
# abre o arquivo exemplo_w.txt em modo escrita (w - write)
# a estrutura "with" lida automaticamente com o fechamento do arquivo 
with open('exemplo_w.txt', 'w') as arquivo:
    # escreve no arquivo 'Ola mundo'
    arquivo.write('Ola mundo\n') # '\n' para pular de linha
    # escreve no arquivo 'linha 2'
    arquivo.write('linha 2' + '\n') # '\n' para pular de linha
    # escreve no arquivo 'Fim do arquivo'
    arquivo.write('Fim do arquivo')
