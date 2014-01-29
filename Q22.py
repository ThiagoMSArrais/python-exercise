#! usr/bin/env python3

#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
#Dica: utilize o operador módulo (resto da divisão)


def verificarNumero():

    try:
        #Solicita um numero inteiro.
        numero = int(input("Por favor, informe um número:"))

        #Verificar se o valor de numero eh PAR ou IMPAR.
        if numero % 2 == 0:
            print ("Par!")
        else:
            print ("Impar!")

    except ValueError:
        print ("Por favor, informe somente um valor numerico.")
        verificarNumero()
