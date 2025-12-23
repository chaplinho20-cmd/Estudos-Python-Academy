from random import choice

def mensagem_perdeu(computador, valor):
    print(f"O computador jogou {computador}! e Você jogou {valor}!")
    print(f'Você Ganhou!!')
    print(f'Vamos Jogar Denovo!! 😠')

def mensagem_venceu(computador, valor):
    print(f"O computador jogou {computador}! e Você jogou {valor}!")
    print(f'Você Perdeu!!😊')

print(f"~=" * 10,{'Impar ou Par'},"~=" * 10)

contador = 0

while True :
    computador = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    valor = int(input("Digite um valor: "))
    escolha = str(input(f'Par ou Ímpar? [P/I]: ')).strip().upper()

    soma = valor + computador

    if escolha == "P" :
        if soma%2 == 0:
            mensagem_perdeu(computador, valor)
        if soma%2 == 1:
            mensagem_venceu(computador, valor)
            break
    if escolha == "I" :
        if soma%2 == 0:
            mensagem_venceu(computador, valor)
            break
        if soma%2 == 1:
            mensagem_perdeu(computador, valor)

    contador += 1

print(f"~=" * 10,'Game Over!! Você venceu',{contador},'Vezes.',"~=" * 10)