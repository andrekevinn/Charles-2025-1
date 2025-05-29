# Tabuada
import sys
try:
    n = int(input('Informe um número inteiro e positivo: '))
    if n <= 0: sys.exit('ERRO: Insira um valor positivo.')
except ValueError: sys.exit('ERRO: Insira um valor que possa ser convertido para inteiro')
multiplicando = 1
while multiplicando <= 10:
    print(f'{n} x {multiplicando} = {n * multiplicando}')
    multiplicando += 1
else: print('Fim da tabuada.')
