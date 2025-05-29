'''Fatorial'''
import sys

try:
    n = int(input('Insira um número inteiro: '))
except ValueError: sys.exit('ERRO: Insira um valor que possa ser convertido para inteiro.')
except Exception as e: print(f'ERRO: {e}')
else: 
    if n < 0: print('Não existe fatorial.') 
    elif n < 2: print(f'{n}! = 1.')
    else:
        fat = n
        naux = n
        while  naux <= 2:
            naux -= 1
            fat *= naux
        print(f'{n}! = {fat}.')