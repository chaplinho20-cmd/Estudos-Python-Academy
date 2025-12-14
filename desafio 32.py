#faça um programa que veja se o ano digitado é bisexto ou não

print('{:=^40}'.format(' '))
print('\033[4m\033[96m{}\033[0m'.format('VEJA SE SEU ANO É BISSEXTO:'))

ano = int(input('Qual o Ano? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Seu ano é bissexto!')

else:
    print("Seu ano não é bissexto!")
