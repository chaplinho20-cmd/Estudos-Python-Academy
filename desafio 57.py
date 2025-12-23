sexo = str(input("Digite o sexo [M/F]: ")).upper()

while sexo != 'M' and sexo != 'F' :
    sexo = str(input('Dados Inválidos. Por Favor,  Insira apenas M ou F :')).upper()
    if sexo == 'M':
        print('Sexo Masculino Cadastrado')
    if sexo == 'F':
        print('Sexo Feminino Cadastrado')
