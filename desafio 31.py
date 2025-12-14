#desenvolva um programa que pergunte a distancia de uma viagem em km calcule o preço da passagem
#cobrando R$0,50 por Km para viagens até 200km e R$o,45 para viagens mais longas

print('{:=^40}'.format(' '))
print('\033[4m\033[96m{}\033[0m\033[96m!!!\033[0m\n'.format('Descubra o Valor de Sua Passsagem'))

viagem = float(input('Qual a distância da viagem? \n'))

if viagem <= 200:
    valor_200km = (viagem * 0.50)
    print('Sua viagem ficou no valor de R${:.2f}!'.format(valor_200km))

else:
    valor_201km = (viagem * 0.45)
    print("Sua viagem ficou no valor de R${:.2f}!".format(valor_201km))
