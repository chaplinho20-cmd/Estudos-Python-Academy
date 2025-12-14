velocidade = int(input('Qual a velocidade do carro? '))

excesso = float(velocidade - 80)

if velocidade > 80:
    multa = excesso * 7
    print('Você foi Multado no valor de R$ {:.2f} por exceder o limite em {} km/h!!'.format(multa, excesso))