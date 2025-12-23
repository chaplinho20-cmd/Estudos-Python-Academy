'''n = int(input('Digite um Número [999 para parar]: '))

contador = 1
parada = False
soma = 0

while not parada:
    repete = int(input('Digite um Número [999 para parar]: '))
    soma += n + repete
    contador += 1
    if repete == 999:
        parada = True

print('Você Digitou {} númetos e a soma entre eles foi {}'.format(contador, soma ))'''

soma = 0
contador = 0

while True:
    n = int(input('Digite um Número [999 para parar]: '))

    if n == 999:
        break

    soma += n
    contador += 1

print(f'Você digitou {contador} números e a soma entre eles foi {soma}')