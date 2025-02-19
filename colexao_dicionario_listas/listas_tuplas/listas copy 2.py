def dobra(x):
    return x**2

numeros=[x for x in range(1,11)]

dobrados = list(map(dobra, numeros))
print(dobrados)
    
    
def ehpar(x):
    return x % 2 == 0

pares=list(filter(ehpar,numeros))
print(pares)