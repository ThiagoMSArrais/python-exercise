#! usr/bin/env python3

# Faça um Programa que leia três números e mostre o maior deles.


def maiorNumero():

    lista_numeros = []

    for x in range(1, 4):

        lista_numeros.append(int(input("Informe um número:")))

    print ("O maior número é " + str(max(lista_numeros)) + ".")

    """
    maior = 0

    for i in lista_numeros:
        
        if lista_numeros[i] > maior:
            maior = lista_numeros[i]

    print ("O maior valor é " str(maior) + ".")

    """
