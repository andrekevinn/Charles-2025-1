# Programa para calcular o movimento retilínio uniformemente variado
# Calcular o tempo de viagem entre Lajes e Natal

import sys

V = int(input(f'Insira a velocidade inicial V em km/h: '))
if V <= 0:  
    sys.exit('Informe velocidade positiva')

t = int(input(f'Insira o tempo t em Seg: '))
if t <= 0:
    sys.exit('Informe tempo positivo')

a = int(input(f'insira o aceleração a em m/s²: '))
if a <= 0:
    sys.exit('Informe aceleração positiva')

DS = (V * t) + (a * t**2)/2
TV = (a * t**2)/2 + (V * t - DS)
MRUV = DS

print(f' A distância DS é: {DS}')
print(f'O tempo de viagem é: {TV}')