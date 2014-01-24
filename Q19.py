#! usr/bin/env python3
#####################################################################
#Faça um Programa que leia um número inteiro menor que 1000 e imprima
#a quantidade de centenas, dezenas e unidades do mesmo.
#
#    Observando os termos no plural a colocação do "e", da vírgula
#    entre outros. Exemplo:
#    326 = 3 centenas, 2 dezenas e 6 unidades
#    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,
#    305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
######################################################################


def numeroExtenso():

    #Lista Ordem dos numeros
    ordemNumerica = ("centena", "dezena", "unidade")

    #lista Caracteres.
    caracteres = (", ", " e ", ".")

    try:
        #Obter um valor numerico.
        numero = input("Informe um valor:")

        #verificar se é menor que 1000.
        if int(numero) < 1000 and int(numero) > 0:
            for x in range(len(numero)):
                print ("%d %s%s" % (int(numero[x]), ordemNumerica[x + (3 - len(numero))] + "s" if int(numero[x]) > 1 else ordemNumerica[x + (3 - len(numero))], caracteres[x + (3 - len(numero))]), end="")                       
			
        else:
            print ("Por favor, informe um valor menor que 1000 e maior que 0.")
            numeroExtenso()
    except ValueError:
        print ("Por favor, informe somente valor numerico.")
        numeroExtenso()

    print()
