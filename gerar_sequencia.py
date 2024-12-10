# Implemente uma função gerar_sequencia_personalizada(inicio, fim, regra)
# que:
# - Receba um intervalo de início e fim
# - Aplique uma regra de transformação personalizada
# - Retorne uma nova lista com os números transformados
# - Algumas regras possíveis:
# - Dobrar o valor
# - Elevar ao quadrado
# - Somar 10
# - Subtrair 5
# Exemplo de entrada: inicio=1, fim=5, regra="dobrar"

def gerar_sequencia_personalizada(inicio, fim, regra):
    if regra == 'dobrar':
        return [x * 2 for x in range(inicio, fim+1)]
    elif regra == 'elevar':
        return [x ** 2 for x in range(inicio, fim+1)]
    elif regra == 'somar':
        return [x + 10 for x in range(inicio, fim+1)]
    elif regra == 'subtrair':
        return [x - 5 for x in range(inicio, fim+1)]
    else:
        print('Regra invalida')
        return[]

print(gerar_sequencia_personalizada(0,10,'dobrar'))
print(gerar_sequencia_personalizada(0,10,'elevar'))
print(gerar_sequencia_personalizada(0,10,'somar'))
print(gerar_sequencia_personalizada(0,10,'subtrair'))
