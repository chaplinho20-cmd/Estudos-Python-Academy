def texto_invert(texto):
    return texto[::-1]

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')

invertida = texto_invert(frase)

if frase == invertida:
    print('Sua frase é um Palindromo!!')
    print(frase)
    print(invertida)
else :
    print('Sua Frase NÂO é um Palindromo!!')
    print(frase)
    print(invertida)
