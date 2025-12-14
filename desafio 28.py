import random

numero = int(input('Adivinhe um numero entre 0 e 5: '))

numero_random = random.randint(0,6)

if numero_random == numero:
    print('Parabens!!! Você acertou!!!')
else:
    print('Tente novamente!! Você errou! o número certo era {}!!'.format(numero_random))