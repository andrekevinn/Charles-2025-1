'''Progama para solicitar ao usuários que digite números inteiros aleatoriamente até digitar 0
Após digitado alguns desses números, o programa deve mostrar
a) a soma de todos números e dos ímpares
b) o produtos de todos números, e dos ímpares
c) a divisão da soma de todos pela soma dos ímpares
d) a divisão do produto de todos pelo produto dos ímpares
e) a quantidade de números digitados.'''
import sys
n = None
soma = 0
somaI = 0
nq = 0
nI = 0
while n != 0:
    try:
        n = int(input('Digite um número inteiro: '))
    except ValueError:
        sys.exit('ERRO: Insira valor capaz de ser convertido para inteiro.')
    except Exception as e:
        print(f'ERRO: {e}')
    else:
        if n != 0:
            nq += 1
            soma += n
        if n % 2 != 0:
            nI += 1
            somaI += n
            

print(f'A quantidade de números digitados foi {nq}.')
print(f'A soma de todos os números é: {soma}.')
print(f'A soma de todos os números é ímpares é: {somaI}.')