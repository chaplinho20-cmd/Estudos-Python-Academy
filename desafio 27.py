#faça um programa que leia o nome completo de uma pessoa.
#mostrando em seguida o primeiro e o ultimo nome separadamente
nome = str(input('Digite seu nome completo: '))

nome_sem_espaco = nome.strip()
nome_title = nome_sem_espaco.title()
nome_lista = nome_title.split()

tamanho = len(nome_lista)

primeiro_nome = nome_lista[0]
ultimo_nome = nome_lista[tamanho-1]

print("Seu preiro nome é: {}".format(primeiro_nome))
print("Seu último nome é: {}".format(ultimo_nome))
