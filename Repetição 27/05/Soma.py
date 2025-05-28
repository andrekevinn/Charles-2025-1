'''Programa para executar um produto de 2 número inteiros positvos utilizando apenas o operador soma (+)'''
import sys
try:
    n1 = int(input('Insira um número inteiro: '))
    n2 = int(input('Insira um número inteiro para multiplicar o primeiro: '))
    if n1 <= 0: 
        sys.exit('ERRO: Insira um valor positivo.')
    if n2 <= 0: 
        sys.exit('ERRO: Insira um valor positivo.')
except ValueError: sys.exit('ERRO: Insira um valor que possa ser convertido para inteiro')
while n1 <= n2: 
    print(f'{n1} + {n2} =  {n1 + n2}')
    + n2
else:
    print('fim')
