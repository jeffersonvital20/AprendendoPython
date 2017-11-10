salario = float(input('Qual é o salrio do funcionário? R$'))
novo = salario + (salario *15/100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passs a receber R${:.2f}'.format(salario, novo))