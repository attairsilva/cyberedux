# 3. Escreva um programa que recebe um número inteiro N e então mostre cada um dos dígitos daquele
# número
# NÃO UTILIZE STRINGS


numero = int(input('Informe um numero inteiro: '))

while numero:
   print(f'{numero % 10}')
   numero = numero // 10
