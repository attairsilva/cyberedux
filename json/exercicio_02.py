import json  
# Importa o módulo JSON para manipular arquivos no formato JSON

def cadastrar_pessoa(dicionario):
    #funcao cadastra pessoa no dicionaio
    cpf=input('Informe o seu CPF: ')
    nome=input('Informe seu nome: ') 
    pessoa = []
    pessoa=nome
    dicionario[cpf]={ "nome": pessoa}

def buscar_pessoas(dicionario):
    #busca pessoa no dicionario
    consulta = int(input('Informe o CPF da pessoa: '))
    cont=0
    for chave, valor in pessoas.items():
        if int(chave) == consulta:
            cont+=1
            print(f'{chave} - Nome: {valor['nome']} ')
        if cont == 0:
            print('Não encontrado!')

def listar_pessoas(dicionario):
    # lista pessoas do dicionario
    for cpf,pessoa in pessoas.items():
                print(f'{cpf} - Nome: {pessoa['nome']} ')

def salvar_pessoas(dicionario):
    # Função para salvar os cadastros em um arquivo JSON
    with open("cadastros.json", "w") as arquivo:  
            # Abre o arquivo para escrita
            json.dump(pessoas, arquivo, indent=4)  
             # Salva a lista de cadastros no arquivo
            print("Cadastros salvos com sucesso no json!")  
            # Confirmação de salvamento

def carregar_pessoas():
    try:
        with open("cadastros.json", "r") as arquivo:
                pessoas = json.load(arquivo)
                print("Carregados o arquivo JSON com sucesso!")
                return pessoas  # Retorna os dados carregados
    except:
        pessoas=[]

def editar_pessoas(dicionario):
    # Edita o nome de uma pessoa já cadastrada
    cpf = input("Informe o CPF da pessoa que deseja editar: ")
    print(f'= Nome Anterior => {dicionario.get(cpf)}')
    if cpf in dicionario:
        novo_nome = input("Informe o novo nome: ")
        dicionario[cpf]['nome'] = novo_nome
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

pessoas=carregar_pessoas()

while True:
    
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
    elif operacao == 2:
        listar_pessoas(pessoas)
    elif operacao == 3:
        editar_pessoas(pessoas)
    elif operacao == 4:
        deletar_pessoas(pessoas)
    elif operacao == 5:
        buscar_pessoas(pessoas)
    elif operacao == 6:
        salvar_pessoas(pessoas)
        break 
    
    else:
        print('Opção inválida!')
