#! usr/bin/env python3

#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


def identificarSemana():

    #tupla relacionado aos dias da semana.
    tuplaSemana = ((1, "Domingo"), (2, "Segunda-feira"), (3, "Terça-feira"), (4, "Quarta-feira"), (5, "Quinta-feira"), (6, "Sexta-feira"), (7, "Sábado"))

    try:
        #capturar um valor numérico para da semana.
        diaSemana = int(input("Por favor, informe um número da semana:"))

    except ValueError:
        print ("Por favor, informe somente valor numérico!")
        identificarSemana()

    #verificar o dia da semana.
    for index, value in enumerate(tuplaSemana):
        #verifica se o diaSemana não é superior ao valor sete.
        if not diaSemana < 7:
            print ("Valor inválido!")
            break
        else:
            if diaSemana == value[0]:
                print ("Hoje é " + value[1])
                break
