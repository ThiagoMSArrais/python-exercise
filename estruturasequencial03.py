#! usr/bin/env python3

#########################################################
#Faça um Programa que peça dois números e imprima a soma.
#########################################################


def somar():

    #lista de números obtidos.
    lista_numero = []
    
    try:
    
        #iterar duas vezes para obter os valores.
        for index in range(2):
            #armazenar o valor numérico em lista_numero.
            lista_numero.append(int(input("Inserir numéro:")))
        
    except ValueError:
        #Imprimir na tela "valor inválido!"
        print ("Valor inválido!")
        
    print ("A soma dos dois números são:{0}".format(sum(lista_numero)))
