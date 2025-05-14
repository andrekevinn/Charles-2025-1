'''Exceções, é importar testar os erros para saber quais tipos de erro colocar no except
# except Exception as XXXX: print(f' ERRO; {XXXX})'''

import sys

try:
    intdividendo = int(input('Digite o dividendo: '))
    intdivisor = int(input('Digite o divisor: '))
    resultado = intdividendo / intdivisor
except ValueError: 
    print(f'ERRO: insira um valor que possa ser convertido em inteiro.')
except ZeroDivisionError:
    print(f'ERRO: Não se pode dividir por zero.')
except:
    print(f'EROO: {sys.exc_info()}')
else:
    print(f'O resultado é: {resultado}')