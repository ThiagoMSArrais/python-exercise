#! usr/bin/env python3

# Faça um Programa que peça dois números e imprima o maior deles.


def comparadorMaiorValor():

    # lista de numeros inteiros.
    numeros = []

    for x in range(2):
        numeros.append(input("Por favor, informe um número:"))

    print (max(numeros))
