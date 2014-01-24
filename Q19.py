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

    try:
        #Obter um valor numerico.
        numero = int(input("Informe um valor:"))

        #numero inteiro menor que 1000.
        if numero < 1000 and numero > 0:
            for x in range(len(str(numero))):
                if len(str(numero)) == 3:
                    print ("%d %s, %d %s e %d %s" % (str(numero[0]), [ordemNumerica[0] + "s" if numero[0] > 1 else ordemNumerica[0]], str(numero[1]), [ordemNumerica[1] + "s" if numero[1] > 1 else ordemNumerica[1]], str(numero[2]),  [ordemNumerica[2] + "s" if numero[2] > 1 else ordemNumerica[2]]))
        else:
            print ("Por favor, informe um valor menor que 1000 e maior que 0.")
            numeroExtenso()
    except ValueError:
        print ("Por favor, informe somente valor numerico.")
        numeroExtenso()

numeroExtenso()
