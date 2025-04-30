# Fazer um programa para solicitar o valor de uma venda e
# o percentual da comissão e eixibir o valor da comissão

valorvenda = float(input('digite o valor da venda (R$): '))
percentual = float(input('digite a comissão (%)...: '))

comissao = (valorvenda * percentual) / 100

print(f'O valor da comissão é R$ {comissao:.2f}')