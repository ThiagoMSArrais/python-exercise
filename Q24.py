#! usr/bin/env python3

########################################################################################################
#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.
########################################################################################################

from collections import namedtuple


def tratarNumeros():

    #dados utilizando tuplas nomeadas.
    Dados = namedtuple("Dados", "numero par_ou_impar positivo_ou_negativo inteiro_ou_decimal")
    
    #fazer o for e obter os valores.
    for i in range(1,3):
        #obter os valores
        numero_capturado = input("Por favor, informe um número:")
        
        #verificar se é par ou ímpar.
        if eval(numero_capturado) % 2 == 0:
            
            
    
