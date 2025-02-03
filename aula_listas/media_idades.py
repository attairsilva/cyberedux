# Crie uma função validar_idades(lista_idades) que:
# - Receba uma lista de idades
# - Verifique se todas as idades são válidas (entre 0 e 120)
# - Retorne uma lista apenas com idades válidas
# - Imprima a quantidade de idades inválidas removidas
# - Calcule a média das idades válidas
# Exemplo de entrada: [25, 17, 150, 42, -3, 65, 88]

def validar_idade(lista_idades):
    idades_validas=[]
    idades_invalidas=0
    for idade in lista_idades:
        if idade >= 0 and idade <= 120:
            idades_validas.append(idade)
        else:
            idades_invalidas+=1
            
    
    # metodos alternativos 
    # idades_validas = [filter(lambda idade: idade >= 0 and <= 120, lista_idades)]
    # idades_validas = [idade for idade in lista_idades if idade >= 0 and idade <= 120]
    
    # metodo alternativo - contagem idade invalidas
    #idades_invalidas = len(lista_idades) - len(idades_validas0)
    print(f'Lista idades válidas: {idades_validas}')
    
    print(f'Qtd. Idades invalidas: {idades_invalidas}')
    
    media_idades = sum(idades_validas) / len(idades_validas)
    print(f'Media idades validas: {media_idades}')

idade=[25, 17, 150, 42, -3, 65, 88]
validar_idade(idade)

