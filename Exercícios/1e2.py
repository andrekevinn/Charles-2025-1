# Programa para calcular o movimento retilínio uniformemente variado
import sys

V = int(input(f'Insira a velocidade inicial V em km/h: '))
if V <= 0:  
    sys.exit('Informe velocidade positiva')
V /= 3.6

t = int(input(f'Insira o tempo t em Seg: '))
if t <= 0:
    sys.exit('Informe tempo positivo')

a = int(input(f'Insira o aceleração a em m/s²: '))
if a <= 0:
    sys.exit('Informe aceleração positiva')

DS = (V * t) + (a * t**2)/2
MRUV = DS

print(f'A DS é: {DS}')

# Questão 2, Desconrir o tempo de viagem T no formato hh:mm:ss
# Converter distância de km para m -> D * = 1000
# Converter a Velociade Inicial V de km/h para m/s -> V / = 3.6 (primeira parte)
# T = (a * T**2)/2 + V * T - d, reescrever como equação do 2 grau e achar o delta (maior ou igual a 0) e a raiz X! 

D = int(input(f'Informe a disntância D em km: '))
if D <= 0:
    sys.exit('Informe distância positiva')
D *= 1000
Delta = V**2 - 4 * a * D
if Delta < 0:
    sys.exit('Não é posssível calcular o tempo')

T = (- V + Delta**0.5)/2*a
Hora = T//3600
T = T % 3600
Minuto = T // 60
Segundo = T % 60


print(f'O Tempo é: {Hora}:{Minuto}:{Segundo}:')