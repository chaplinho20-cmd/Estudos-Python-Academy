import random

numero = int(input('Adivinhe o Número de 0 a 10 que pensei, acha que consegue !!!\nQual o seu palpite?  '))

numero_random = random.randint(0,10)

contador = 1

print(numero_random)

while numero < numero_random:
    print('Um pouco Mais!! ')
    tentativa = int(input('Qual sua Proxima escolha? '))

while numero > numero_random:
    print('Ta muito calma guerreiro!! ')
    tentativa = int(input('Qual sua Proxima escolha? '))

if numero == numero_random:
    print('Ae sim Pai, você acertou em {} tentativas ')
    contador += 1
    print('Tentativa {}'.format(contador))
