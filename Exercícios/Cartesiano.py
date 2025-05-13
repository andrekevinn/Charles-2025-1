'''  Programa para informar em qual quadrante cartesiano o ponto está.

   - O programa deverá solicitar as duas coordenadas (x,y) de um ponto;

   - O ponto está no 1º quadrante quando X e Y forem positivos;
   - O ponto está no 2º quadrante quando X for negativo e Y for positivo;
   - O ponto está no 3º quadrante quando X e Y forem negativos;
   - O ponto está no 4º quadrante quando X for positivo e Y for negativo; '''

import sys

x = float(input('Insira a coordenada x: '))
y = float(input('Insira a coordenada y: '))
if x > 0 and y > 0:
    print('Está no 1º Quadrante.')
elif x < 0 and y > 0:
    print('Está no 2º Quadrante.')
elif x < 0 and y < 0:
    print('Está no 3º Quadrante.')
elif x > 0 and y < 0:
    print('Está no 4º Quadrante.')
else:
    print('O ponto está na origem dos eixos coordenados.')