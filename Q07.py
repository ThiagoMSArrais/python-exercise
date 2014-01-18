#! usr/bin/env python3

# Faça um Programa que leia três números e mostre o maior e o menor deles.


def maiorMenor():

    lista_numeros = []

    for x in range(1, 4):

        lista_numeros.append(int(input("Informe um valor:")))

    print("Maior valor: " + str(max(lista_numeros)) + " e menor valor: " + str(min(lista_numeros)))
