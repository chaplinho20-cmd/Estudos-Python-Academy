#faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor entre eles

print('{:=^40}'.format(' '))
print("\033[4m\033[96m{}\033[0m".format('Escolha 3 numeros e saiba quem é o maior e o menor entre eles:'))

numero_1 = float(input('Qual o primeiro numero: '))
numero_2 = float(input('Qual o segundo numero: '))
numero_3 = float(input('Qual o terceiro numero: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    print('{} é o maior'.format(numero_1))
elif numero_2 > numero_1 and numero_2 > numero_3:
    print('{} é o maior'.format(numero_2))
elif numero_3 > numero_1 and numero_3 > numero_2:
    print('{} é o maior'.format(numero_3))

if numero_3 < numero_1 and numero_3 < numero_2 :
    print('{} é o menor'.format(numero_3))
elif numero_2 < numero_1 and numero_2 < numero_3:
    print('{} é o menor'.format(numero_2))
elif numero_1 < numero_2 and numero_1 < numero_3:
    print('{} é o menor'.format(numero_1))
