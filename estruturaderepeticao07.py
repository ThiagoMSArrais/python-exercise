#! usr/bin/env python3

##############################################################
#Faça um programa que leia 5 números e informe o maior número.
##############################################################


def ler_numeros():

    #lista de números.
    lista_numeros = []
    
    #inicializar o looping com cinco iterações.
    for x in range(5):
    
        try:
        
            #armazenar os números obtidos na lista_numeros.
            lista_numeros.append(int(input("Numero:")))
        
        except ValueError:
            #informar que o valor está errado.
            print ("Valor inválido!")
            x -= 1
            continue

    print ("Maior número:" + str(max(lista_numeros)))
