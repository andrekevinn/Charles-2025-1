'''Faça um programa que solicite ao usuário números inteiros aleatoriamente até que seja informado 0'''
'''Quando for digitado 0 o programa deverá informar
a) Quantos números inteiros foram digitados
b) A soma dos números inteiros positivos
c) A média dos números inteiros positivos

O valor digitado não deve ser considerado em nenhum dos intens acima.'''
import sys

int = None
numdig = 0
nump = 0
while int != 0:
    try:
        int = int(input('Insira um número inteiro: '))
    except ValueError:
        print('ERRO: Insira um valor válido')
    else: 
        if int > 0:
            print('')
        


