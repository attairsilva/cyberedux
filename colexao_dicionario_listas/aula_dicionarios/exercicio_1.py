# Exercício 1 – Faca um programa que permite o usuário cadastrar o
# nome e CPF de pessoas utilizando um dicionário (CPF como
# chave), permita o cadastro ate que o usuário escolha sair do
# programa, antes de sair do programa mostre os CPFs e nomes
# cadastrados.
# Exercício 2 – Incremente o programa do exercício anterior para
# permitir que o nome da pessoa seja procurado através do CPF.


def cadastrar_pessoa(dicionario):
    cpf=input('Informe o seu CPF: ')
    nome=input('Informe seu nome: ')
    
    pessoa = []
    pessoa=nome
     
    dicionario[cpf]=pessoa

pessoas={}
while True:
    print('==================================')
    print('CADASTRO E CONTROLE - CPF')
    print('1 - Incluir Pessoa')
    print('2 - Buscar Pessoa por CPF')
    print('3 - Sair')
    print('==================================')
    operacao = int(input('Informe o numero da opção: '))
    if operacao == 1:
        cadastrar_pessoa(pessoas)
    elif operacao == 2:
        consulta = int(input('Informe o CPF da pessoa: '))
        cont=0
        for chave, valor in pessoas.items():
            if int(chave) == consulta:
                cont+=1
                print(f'==> CPF: {chave} - Nome: {valor} ')
        if cont == 0:
            print('Não encontrado!')
    elif operacao == 3:
        for chave,valor in pessoas.items():
                print(f'==> CPF {chave} - Nome: {valor} ')
        print('Saindo do programa ...') 
        break 
    else:
        print('Opção inválida!')
