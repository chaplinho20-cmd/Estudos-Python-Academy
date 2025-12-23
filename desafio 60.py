numero = int(input('Calcule seu Fatorial: '))

c = numero
f = 1

print('calculando {}! = '.format(numero), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
