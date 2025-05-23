'''  Programa para calcular a distância entre dois pontos no plano cartesiano.

   - O programa deverá solicitar as duas coordenadas (xA,yA) do ponto A;
   - O programa deverá solicitar as duas coordenadas (xB,yB) do ponto B;

   - Calcular a distância entre os pontos (qual fórmula usar????) '''
import sys

try: 
   xA = int(input('Insira a coordenada x do ponto A: '))
   yA = int(input('Insira a coordenada y do ponto A: '))
   xB = int(input('Insira a coordenada x do ponto B: '))
   yB = int(input('Insira a coordenada y do ponto B: '))
except ValueError:
   print(f'ERRO: insira um valor que possa ser convertido para inteiro.')
# Fómrula de distância euclidiana
else:
   dist = (((xB - xA) **2) + ((yB - yA) **2)) ** 0.5
print(f'A distância entre o ponto A e ponto B é: {dist:.0f}')