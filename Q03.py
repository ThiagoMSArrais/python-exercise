#! usr/bin/env python3

# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


def verificadorSexo():
    sexo = input("Informe o sexo (F ou M):")

    if sexo.upper() == "F":
        print ("Feminino!")

    elif sexo.upper() == "M":
        print ("Masculino!")

    else:
        print ("Sexo inválido, informe \"F\" ou \"M\"")
        verificadorSexo()
