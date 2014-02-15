#! usr/bin/env python3

####################################################################
#Faça um programa que receba dois números inteiros e gere os números
#inteiros que estão no intervalo compreendido por eles. 
####################################################################


#solicita duas vezes os numeros para que possar ser armazenados.
lista_numeros = [int(input("Numero:")) for x in range(2)]
#faz iteracao para obter a sequencia dos numeros.
intervalo = [x for x in range(min(lista_numeros),max(lista_numeros))]

#imprimir na tela o intervalo.
print (intervalo)
