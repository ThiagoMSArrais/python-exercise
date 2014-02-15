#! usr/bin/env python3

#############################################################################
#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
#############################################################################


def imprimir_impares():

    #lista com numeros impares entre 1 e 50.
    lista_impares = [x for x in range(1,50) if x % 2 != 0]

    print (lista_impares)
