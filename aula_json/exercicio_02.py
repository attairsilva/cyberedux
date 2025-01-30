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

def editar_pessoas(dicionario):
    # Edita o nome de uma pessoa já cadastrada
    cpf = input("Informe o CPF da pessoa que deseja editar: ")
    if cpf in dicionario:
        novo_nome = input("Informe o novo nome: ")
        dicionario[cpf] = novo_nome
        print("Cadastro atualizado com sucesso!")
    else:
        print("CPF não encontrado!")

def deletar_pessoas(dicionario):
    # Remove uma pessoa do dicionário
    cpf = input("Informe o CPF da pessoa que deseja excluir: ")
    if cpf in dicionario:
        dicionario.pop(cpf)
        print("Cadastro removido com sucesso!")
    else:
        print("CPF não encontrado!")

while True:
    pessoas=carregar_pessoas()
    print("\nMenu de Opções:")
    print("1. Incluir pessoa")  
    print("2. Listar cadastros de pessoas")  
    print("3. Editar Pessoa")  
    print("4. Deletar Pessoa") 
    print("5. Buscar pessoa no dicionario") 
    print('6. Sair')
    print('==================================')
    operacao = int(input('Informe o numero da opção: '))
    if operacao == 1:
        cadastrar_pessoa(pessoas)
        salvar_pessoas(pessoas)
    elif operacao == 2:
        listar_pessoas(pessoas)
    elif operacao == 3:
        editar_pessoas(pessoas)
        salvar_pessoas(pessoas)
    elif operacao == 4:
        deletar_pessoas(pessoas)
        salvar_pessoas(pessoas)
    elif operacao == 5:
        buscar_pessoas(pessoas)
    elif operacao == 6:
        break 
    else:
        print('Opção inválida!')
