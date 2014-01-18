#! usr/bin/env python3

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def valorNumero():

    try:
        num = int(input("Informe um valor:"))

        if num == 0:
            print ("O valor %d é neutro" % num)

        elif num > 0:
            print ("O valor %d é positivo" % num)

        else:
            print ("O valor %d é negativo" % num)

    except ValueError:
        print ("Informe somente número!")
        valorNumero()
