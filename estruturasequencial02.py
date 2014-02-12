#! usr/bin/env python3

###############################################################################################
#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
###############################################################################################


def capturar_numero():

    try:
    
        #obter o valor numérico.
        numero = int(input("Informe um número:"))
        
    except ValueError:
        #Imprimir na tela "valor inválido!"
        print ("Valor inválido!")
        capturar_numero()
        
    #imprimir o valor obtido.
    print ("O número informado foi {0}.".format(numero))
    
