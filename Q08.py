#! usr/bin/env python3

# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


def consultarMenorPreco():

    lista_preco = []

    for i in range(1, 4):

        lista_preco.append(float(input("%d) Informe o preço:" % i)))

    print ("O menor preço R$%.2f" % min(lista_preco))
