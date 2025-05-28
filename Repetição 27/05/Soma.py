'''Programa para executar um produto de 2 número inteiros positvos utilizando apenas o operador soma (+)'''
import sys
try:
    n1 = int(input('Insira um número inteiro: '))
    n2 = int(input('Insira um número inteiro para multiplicar o primeiro: '))
except ValueError: sys.exit('ERRO: Insira um valor que possa ser convertido para inteiro')
else:
    if n1 <= 0: 
        sys.exit('ERRO: Insira um valor positivo.')
    if n2 <= 0: 
        sys.exit('ERRO: Insira um valor positivo.')

    produto = 0
    contador = 1
    while contador <= n2:
        produto += n1
        contador += 1

    print(f'{n1} x {n2} = {produto}')
