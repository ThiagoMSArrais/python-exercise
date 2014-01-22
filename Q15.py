#! usr/bin/env python3

##################################################################################
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
#se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
#se o mesmo é: equilátero, isósceles ou escaleno.
#
#    Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
#que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;
###################################################################################

def analisarTriangulo():

    #listaNumeros
    listaLados = []

    #obter três números.
    for x in range(1,4):
        listaLados.append(int(input("%d)Informe um número:" % x)))

    #analisar os lados.
    if (listaLados[0] == listaLados[1]) and (listaLados[0] == listaLados[2]):
        print ("Triângulo Equilátero.")

    elif (listaLados[0] == listaLados[1] or listaLados[0] == listaLados[2]) or listaLados[1] == listaLados[2]:
        print ("Triângulo Isósceles.")
    else:
        print ("Triângulo Escaleno.")

