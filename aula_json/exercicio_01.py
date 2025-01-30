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
    try:
        with open("cadastros.json", "w") as arquivo:  
            # Abre o arquivo para escrita
            json.dump(pessoas, arquivo, indent=4)  
             # Salva a lista de cadastros no arquivo
            print("Cadastros salvos com sucesso no json!")  
            # Confirmação de salvamento
    except Exception as e:
        print(f"Erro ao salvar cadastros no arquivo json: {e}")  
        # Exibe mensagem de erro caso algo dê errado

def carregar_pessoas():
    #funcao carrega pessoas do arquivo json para lista
    with open("cadastros.json", "r") as arquivo: 
        # Abre o arquivo para leitura
        pessoas = json.load(arquivo) 
        return pessoas 
        #return pessoas


pessoas={}

while True:
    print("\nMenu de Opções:")
    print("1. Incluir pessoa no dicionario")  
    print("2. Listar cadastros do dicionario")  
    print("3. Buscar pessoa no dicionario") 
    print("4. Salvar cadastros do dicionario no json") 
    print("5. Carregar cadastros do json") 
    print('6. Sair')
    print('==================================')
    operacao = int(input('Informe o numero da opção: '))
    if operacao == 1:
        cadastrar_pessoa(pessoas)
    elif operacao == 2:
        listar_pessoas(pessoas)
    elif operacao == 3:
        buscar_pessoas(pessoas)
    elif operacao == 4:
        salvar_pessoas(pessoas)
    elif operacao == 5:
        pessoas=carregar_pessoas() 
    elif operacao == 6:
        break 
    else:
        print('Opção inválida!')
