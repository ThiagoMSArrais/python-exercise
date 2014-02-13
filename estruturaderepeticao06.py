#! usr/bin/env python3

################################################################################
#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
#Depois modifique o programa para que ele mostre os números um ao lado do outro.
################################################################################


def imprimir_numeros():

    #fazer o looping.
    for x in range(2):
        #criar um looping mais interno.
        for y in range(20):
            #imprimir o valor em horizontal e depois em vertical,
            #utilizando uma condição, para poder mudar a posição.
            print (int(x + 1), end=' ' if x == 1 else print())
