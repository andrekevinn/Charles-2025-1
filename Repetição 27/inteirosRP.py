'''Faça um programa que solicite ao usuário números inteiros aleatoriamente até que seja informado 0'''
'''Quando for digitado 0 o programa deverá informar
a) Quantos números inteiros foram digitados
b) A soma dos números inteiros positivos
c) A média dos números inteiros positivos

O valor digitado não deve ser considerado em nenhum dos intens acima.'''
import sys

valor          = None
intSomaPositivos  = 0
intQtValores      = 0
intQtValPositivos = 0

while valor != 0:
    try:
        valor = int(input('Informe um valor inteiro: '))
    except ValueError:
        print('ERRO: Valor Inteiro Inválido...') 
    except Exception as e:
        print(f'ERRO: {e}')
    else:
        if valor > 0:
            intSomaPositivos  += valor
            intQtValPositivos += 1

        if valor != 0:
            intQtValores += 1
   
print(f'Quantos números inteiros foram digitados: {intQtValores}')
print(f'Soma dos números inteiros positivos.....: {intSomaPositivos}')
print(f'Média dos números inteiros positivos....: {intSomaPositivos/intQtValPositivos}')
        


