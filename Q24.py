#! usr/bin/env python3

########################################################################################################
#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.
########################################################################################################


def tratarNumeros():

    #lista de numeros.
    lista_numeros = []
    
    #fazer o for e obter os valores.
    for i in range(1,3):
        #obter os valores
        lista_numeros.append(input("Por favor, informe um número:"))
        
        #verificar se é par ou ímpar.
        if lista_numeros[i] % 2 == 0:
            
    
