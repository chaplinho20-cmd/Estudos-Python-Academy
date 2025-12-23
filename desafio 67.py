numero = 0

while True:
    valor = int(input("Quer ver a tabuada de qual valor: "))
    if valor < 0:
        break
    print(f"Tabuada de {valor}!!\n")
    for numero in range(1, 11):
        print(numero, "x", valor, "=", numero * valor)
        print("-" * 10)

print("Tabuada finalizada!")