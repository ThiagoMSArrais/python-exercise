#! usr/bin/env python3

#############################################################################################################
#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
#############################################################################################################


def verificar_nota():

    while True:
        #obter o número.
        numero = int(input("Informe número:"))
    
        #verificar se o número está entre zero a dez.
        if numero <= 10 and numero >= 0:
            break
            
        else:
            print("Valor inválido!")
            continue
            
    
