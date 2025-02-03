import json
from datetime import date

# Carrega o arquivo de vendas do e cria a estrutura 'vendas' (se o arquivo existir)
#-------------------------------------------------------------------------------
try:
    nome_arquivo_vendas = 'vendas' + date.today().isoformat() + '.json'
    with open(nome_arquivo_vendas, 'r') as arquivo_vendas:
       vendas = json.load(arquivo_vendas)
except:
    # Caso o arquivo não exista, iniciar uma estrutura em branco
    vendas = []
       
# Função para mostrar o recibo formatado
#-------------------------------------------------------------------------------
def mostrar_recibo(lista_vendas):
   
    maxDigitosQnt = max(len(str(round(venda[0], 3))) for venda in lista_vendas)   
    maxDigitosDescricao = max(len(venda[1]) for venda in lista_vendas) 
    maxDigitosPreco = max(len(str(round(venda[2], 2))) for venda in lista_vendas)   

    total = 0
    print('======= RECIBO DE VENDA =======')
    for venda in lista_vendas:
        qnt = str(round(venda[0], 3))
        descricao = venda[1]
        preco = str(round(venda[2], 2))
        total += venda[2]

        espacoQnt = ' ' * (maxDigitosQnt - len(qnt))
        espacoDescricao = ' ' * (maxDigitosDescricao - len(descricao))
        espacoPreco = ' ' * (maxDigitosPreco - len(preco))

        print(f'{espacoQnt}{qnt} - {descricao}{espacoDescricao}  R$ {espacoPreco}{preco}')

    total = str(round(total, 2))
    espaco = ' ' * (maxDigitosQnt + maxDigitosDescricao)
    espacoPreco = ' ' * (maxDigitosPreco - len(total))
    print(f'\nTotal{espaco}R$ {espacoPreco}{total}')
    print('=============================')

# Efetuar venda
#-------------------------------------------------------------------------------
def efetuar_venda():
    # Faça aqui o código de efetuar venda.
    
    print("==== LISTA DE PRODUTOS ===")
    with open('produtos.json', 'r') as arquivo_produtos:
        produtos = json.load(arquivo_produtos)
    for codigo, produto in produtos.items():
        print(f"COD [{codigo}] - {produto['nome']} - Valor R$ {produto['preco']}") 
    
    print("==== INFOME O CODIGO DO PRODUTO A SER VENDIDO ")
   
    vendasatual = []
    
    while True:
        
        codigocheck = input("Informe o códgio do produto: ")
        
        
        if codigocheck == "":
            mostrar_recibo(vendasatual) 
            salvar_vendas(vendas)               
            break
        elif codigocheck in produtos:
            qtd = float(input("Informe a quantidade: "))
            
            if qtd <= 0:
                print("O sistema não aceita quantidade negativa!")
                continue #início do loop
            
            nomep_lista = produtos[codigocheck]["nome"]
            valorp_lista = produtos[codigocheck]["preco"]
            preco_total =  valorp_lista * qtd
            
            vendas.append((qtd, nomep_lista, preco_total))
            vendasatual.append((qtd, nomep_lista, preco_total))
            # Adiciona a nova venda à lista existente
            
        else:
            print("Produto não cadastrado")

# Balancete
#-------------------------------------------------------------------------------
def balancete():
    # Faça aqui o código de balancete
    with open(nome_arquivo_vendas, "r") as arquivo:
            vendasdodia = json.load(arquivo)
            
    print('========= BALANCE DE VENDAS DO DIA ==========')
    
    maxDigitosQnt = max(len(str(round(venda[0], 3))) for venda in vendasdodia)   
    maxDigitosDescricao = max(len(venda[1]) for venda in vendasdodia) 
    maxDigitosPreco = max(len(str(round(venda[2], 2))) for venda in vendasdodia)   

    total = 0

    for venda in vendasdodia:
        qnt = str(round(venda[0], 3))
        descricao = venda[1]
        preco = str(round(venda[2], 2))
        total += venda[2]

        espacoQnt = ' ' * (maxDigitosQnt - len(qnt))
        espacoDescricao = ' ' * (maxDigitosDescricao - len(descricao))
        espacoPreco = ' ' * (maxDigitosPreco - len(preco))

        print(f'{espacoQnt}{qnt} - {descricao}{espacoDescricao}  R$ {espacoPreco}{preco}')

    total = str(round(total, 2))
    espaco = ' ' * (maxDigitosQnt + maxDigitosDescricao)
    espacoPreco = ' ' * (maxDigitosPreco - len(total))
    print(f'\nTotal{espaco}R$ {espacoPreco}{total}')

# Salvar arquivo de vendas
#-------------------------------------------------------------------------------
def salvar_vendas(dicionario):
    # Função para salvar em um arquivo JSON
    with open(nome_arquivo_vendas, "w") as arquivo:  
            # Abre o arquivo para escrita
            json.dump(vendas, arquivo, indent=4)  
             # Salva alista no arquivo
            print("Cadastros salvos com sucesso no arquivo de vendas diario")  
            # Confirmação de salvamento

# Menu
#-------------------------------------------------------------------------------
def menu():
    while True:
        print('1 - Efetuar Venda')
        print('2 - Balancete')
        print('0 - Sair')
        
        opc = input('Digite a opção: ')

        if opc == '1':
            # Efetuar venda
            efetuar_venda()
        elif opc == '2': 
            # Balancete
            balancete()
        elif opc == '0':
            # Sair
            break
        else:
            # Opção inválida
            print(f'Opção {opc} é inválida')

        

# Chama a função menu
#-------------------------------------------------------------------------------
menu()

