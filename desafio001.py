"""Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
"""

valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite o seu salário: "))
anos = int(input("Digite a quantidade de parcelas que deseja: "))

valor_prestacao = valor_casa/(anos*12)

if valor_prestacao > (salario_comprador * 0.30):
    print("O valor excede o permitido para o empréstimo ")
else:
    print("Empréstimo aprovado")