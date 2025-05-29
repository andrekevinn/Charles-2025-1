'''Dado os números primos, faça um programa que solicite ao usuário um número inteiro e informe se é primo ou não'''
import sys

try:
    n = int(input('Insira um número inteiro e positvo: '))
    if n <= 0: sys.exit('ERRO: Insira um número inteiro e positivo.')
except ValueError: sys.exit('ERRO: Insira um valor que possa ser convertido para inteiro.')
except Exception as e: print(f'ERRO: {e}')
else:
    ndd = 1
    divisor = 2
while divisor <= n:
    if n % divisor == 0:
        ndd += 1
    if ndd > 2: break
    divisor += 1
if ndd == 2:
    print('Primo')
else:
    print('Não primo')