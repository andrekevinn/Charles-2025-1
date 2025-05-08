''' Programa para classificar um triângulo quantos aos ângulos.
 - O programa deverá solicitar 3 ângulos inteiros positivos;
 = Para ser um triângulo, a soma dos ângulos deve ser igual a 180;

 - Retângulo: possui um ângulo interno reto (igual a 90).
 - Obtusângulo: possui um ângulo interno obtuso (maior que 90).
 - Acutângulo: possui todos os ângulos internos agudos (menores que 90).
'''
import sys

a1 = int(input('insira o valor do ângulo 1: '))
if a1 <= 0:
    sys.exit('informe ângulo positivo')

a2 = int(input('insira o valor do ângulo 2: '))
if a2 <= 0:
    sys.exit('informe ângulo positivo')

a3 = int(input('insira o valor do ângulo 3: '))
if a3 <= 0:
    sys.exit('informe ângulo positivo')

# Triângulos 

T = a1 + a2 + a3
if T < 180 or T > 180:
    sys.exit('Não é um triângulo')
