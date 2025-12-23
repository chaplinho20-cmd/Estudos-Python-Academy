resp = 'S'
media = soma = quant = maior = menor = 0

while resp in 'S':
    numero = int(input('digite um numero: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('deseja continuar? [S/N] ')).upper().strip()[0]

media = soma / quant

print('Voce digitou {} numeros e a media entre eles é {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
