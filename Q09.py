#! usr/bin/env python3

# Faça um Programa que leia três números e mostre-os em ordem decrescente.


def ordenarDecrescente():
    # lista de numeros inteiros.
    lista_numeros = []
    
    for i in range(0, 4):

        lista_numeros.append(int(input("%d Informe um número:" % i)))

    print ("Numeros decrescentes " + sorted(lista_numeros, reverse=True)
