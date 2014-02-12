#! usr/bin/env python3

##################################################################
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
##################################################################


def media_prova():

    #uma lista para armazenar números.
    lista_numeros = []
    
    try:
    
        #iterar quatro vezes para solicitar os números para armazenar.
        for index in range(4):
            #solicitar um valor e armazená-lo na lista_numeros.
            lista_numeros.append(float(input("Informe a nota:")))
            
    except ValueError:
        #Imprimir na tela o "valor inválido".
        print ("Valor inválido!")
        media_prova()
        
    #calcular a média.
    media = sum(lista_numeros) / len(lista_numeros)
    
    #Imprimir na tela o resultado da média.
    print ("Média: %.1f" % media)
