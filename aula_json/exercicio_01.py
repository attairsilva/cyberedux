import json  
# Importa o módulo JSON para manipular arquivos no formato JSON

import json  
# Importa o módulo JSON para manipular arquivos no formato JSON

def cadastrar_pessoa(dicionario):
    #funcao cadastra pessoa no dicionaio
    cpf=input('Informe o seu CPF: ')
    nome=input('Informe seu nome: ') 
    pessoa = []
    pessoa=nome
    dicionario[cpf]=pessoa

def buscar_pessoas(dicionario):
    #busca pessoa no dicionario
    consulta = int(input('Informe o CPF da pessoa: '))
    cont=0
    for chave, valor in pessoas.items():
        if int(chave) == consulta:
            cont+=1
            print(f'==> CPF: {chave} - Nome: {valor} ')
        if cont == 0:
            print('Não encontrado!')

def listar_pessoas(dicionario):
    # lista pessoas do dicionario
    for chave,valor in pessoas.items():
                print(f'==> CPF {chave} - Nome: {valor} ')

def salvar_pessoas(dicionario):
    # Função para salvar os cadastros em um arquivo JSON
    with open("cadastros.json", "w") as arquivo:  
            # Abre o arquivo para escrita
            json.dump(pessoas, arquivo, indent=4)  
             # Salva a lista de cadastros no arquivo
            print("Cadastros salvos com sucesso no json!")  
            # Confirmação de salvamento

def carregar_pessoas():
    with open("cadastros.json", "r") as arquivo:
            pessoas = json.load(arquivo)
            print("Carregados o arquivo JSON com sucesso!")
            return pessoas  # Retorna os dados carregados

pessoas={}    
   
while True:
        # Loop principal do programa
        pessoas=carregar_pessoas()
        print("\nMenu de Opções:")
        print("1. Incluir pessoa")  
        print("2. Listar cadastros de pessoas")  
        print("3. Editar Pessoa")  
        print("4. Deletar Pessoa") 
        print("5. Buscar pessoa no dicionario") 
        print('6. Sair')
        print('==================================')
        opcao = int(input('Informe o numero da opção: '))
        if opcao == 1:
            cadastrar_pessoa(pessoas)  # Chama a função para cadastrar pessoa
        elif opcao == 2:
            listar_pessoas(pessoas)  # Chama a função para listar os cadastros
        elif opcao == 3:
            salvar_pessoas(pessoas)  # Chama a função para salvar os cadastros
        elif opcao == 4:
            carregar_pessoas()  # Chama a função para carregar os cadastros
        elif opcao == 5:
            print("Saindo do programa. Até mais!")  # Mensagem de saída
            break  # Encerra o loop e finaliza o programa
        else:
            print("Opção inválida. Tente novamente.") 
            # Mensagem para opções inválidas


