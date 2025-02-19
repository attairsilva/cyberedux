# Desenvolva um sistema de análise de desempenho acadêmico que:
# - Receba uma lista de notas de um aluno
# - Calcule a média final
# - Identifique o número de notas abaixo de 7.0
# - Determine o conceito final:
# A: média >= 9.0
# B: 8.0 <= média < 9.0
# C: 7.0 <= média < 8.0
# D: média < 7.0
# - Imprima um relatório detalhado
# Exemplo de entrada: [8.5, 7.2, 9.0, 6.5, 8.0]

notas=[8.5, 7.2, 9.0, 6.5, 8.0]


#metodo 01
media = 0
for nota in notas:
    media += nota
media /= len(notas)
print(f'Media metodo 01: {media}')

#metodo 02
media_02 = sum(notas) / len(notas)
print(f'Media metodo 02: {media_02}')

#notas abaixo de 7

#metodo 01 
notas_abaixo_7=sum(1 for nota in notas if nota < 7.0)

#metodo 02
notas_abaixo7=0
for nota in notas:
    if nota < 7.0:
        notas_abaixo7 += 1


# A: média >= 9.0
if media >= 9.0:
    conceito='B'
# B: 8.0 <= média < 9.0
elif media >= 8.0 and media < 9.0:
    conceito='B'
# C: 7.0 <= média < 8.0
elif media >= 7.0 and media < 8.0:
    conceito='C'
# D: média < 7.0
elif media < 7.0:
    conceito='D'

print(f'Notas: {notas} ')
print(f'Notas menor 7: {notas_abaixo7} ')
print(f'Média: {media} ')
print(f'Conceito: {conceito} ')