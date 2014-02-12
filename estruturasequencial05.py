#! usr/bin/env python3

#######################################################
#Faça um Programa que converta metros para centímetros#
#######################################################


def converter_comprimento():

    #obter o valor de comprimento.
    valor_comprimento = int(input("Informe o valor:"))
    
    #fazer a conversão de unidades.
    conversao = valor_comprimento * 100
    
    #imprimir na tela o resultado da conversão.
    print ("Resultado %dcm" % conversao)
    

    
