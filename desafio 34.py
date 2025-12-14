#escreva um progama que pergunte o salario de um funcionario e calcule o aumento de 10% para salaio superiores a 1250
#e 15% para salarios inferiores

print('{:=^40}'.format(' '))
print('\033[4m\033[96m{}\033[0m\n'.format('Veja Seu salário com almento:'))

salario = float(input('Informe seu Salário atual: '))

salario_10 = (salario * 0.10)
salario_15 = (salario * 0.15)

if salario > 1250.00:
    aumento1 = salario_10 + salario
    print('\nSeu Aumento foi R$ {:.2f} , Totalizando um salário de R$ {:.2f}'.format(salario_10, aumento1))

elif salario <= 1250.00:
    aumento2 = salario_15 + salario
    print('\nSeu Aumento foi R$ {:.2f} , Totalizando um salário de R$ {:.2f}'.format(salario_15, aumento2))
