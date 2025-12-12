cidade = str(input("Em que cidade você nasceu? "))

cidade_sem_espaco = cidade.strip()
cidade_finalizado = cidade_sem_espaco.title()
cidade_dividida = cidade_finalizado.split()

tem_santo = cidade_dividida[0] == "Santo"

print(cidade_finalizado)
print(tem_santo)