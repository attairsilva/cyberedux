def cadastrar_carro(dicionario):
    placa=input('Placa do carro: ')
    marca=input('Marca do carro: ')
    modelo=input('Modelo do carro: ')
    ano=input('Ano do carro: ')
    cor=input('Cor do carro: ') 
    
    carro = {}
    carro[marca]=marca
    carro[modelo]=modelo
    carro[ano]=ano
    carro[cor]=cor
    
    
    
    dicionario[placa]=carro


carros={}
cadastrar_carro(carros)

    