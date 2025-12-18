from datetime import date

print('Escreva os anos de Nascimento: ')

ano_atual = date.today().year

qtd_maiores = 0
qtd_menor = 0
for i in range(7):
    ano_nascimento = int(input(f'Nascimento {i + 1}: '))
    if ano_atual - ano_nascimento >= 18:
        qtd_maiores += 1
    else :
        qtd_menor += 1

print('ja atingiram a maior idade {}'.format(qtd_maiores))
print('ainda não atingiram a maior idade {}'.format(qtd_menor))
