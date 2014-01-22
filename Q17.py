#! usr/bin/env python3

####################################################################
#Faça um Programa que peça um número correspondente a um
#determinado ano e em seguida informe se este ano é ou não bissexto.
####################################################################

def verificarAnoBissexto():

    #obter um valor numérico.
    try:
        numero = int(input("Informe um valor:"))

    except ValueError:
        print ("Por favor, informe um valor numérico!")
        verificarAnoBissexto()

    if (numero % 4 == 0 and numero % 100 != 0) or numero % 400 == 0:
        print ("Ano Bissexto.")
    else:
        print ("Não é Ano Bissexto") 
verificarAnoBissexto() 
