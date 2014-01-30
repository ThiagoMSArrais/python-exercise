#! usr/bin/env python3

#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.


def verificarTipoNumero():

    try:

        #obter valor.
        numero = input("Informe um valor:")

        #verificar qual tipo numerico.
        if isinstance(eval(numero), int):
            print ("Número inteiro!")

        elif isinstance(eval(numero), float):
            print ("Número decimal!")

    except NameError:
        print ("Valor inválido!")
        verificarTipoNumero()
