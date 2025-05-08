''' Progama para calcular a média de uma disciplina semestral no IFRN
As notas devem ser inteiras entre 0 e 100 (inclusive).
Caso a média seja igual ou superior a 60 o aluno estará aprovado; Caso a média seja igual ou superior a 20 o aluno estará em Prova Final, e os demais casos o aluno estará reprovado'''
import sys

# Etapa 1
e1 = int(input('Informe a nota da etapa 1: '))
if e1 < 0 or e1 > 100:
    sys.exit('ERRO: Nota e1 inválida. Informe nota entre 0 e 100')

# Etapa 2
e2 = int(input('Informe a nota da etapa 2: '))
if e2 < 0 or e2 > 100:
    sys.exit('ERRO: Nota etapa da 2 inválida. Informe nota entre 0 e 100')

# Médoa
media = int(round((e1*2 + e2*3)/5, 0))
print(f'Média do Aluno: {media}')

# Verificando situação
if media >= 60:
    print('Aluno Aprovado.')
elif media >= 20:
    print('Aluno em Prova Final.')
else:
    print('Aluno Reprovado.')
