#! usr/bin/env python3

##########################################################################
#Faça um programa que lê as duas notas parciais obtidas por um aluno numa
#disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
##########################################################################


def analisarNotas():

    #tupla media de aproveitamento.
    mediaAproveitamento = ((9.0, 10.0, 'A'), (7.5, 9.0, 'B'), (6.0, 7.5, 'C'), (4.0, 6.0, 'D'), (0, 4.0, 'E'))

    #Obter as duas notas da prova.
    listaNotas = []
    for x in range(1,3):
        listaNotas.append(float(input("%d)Informe a sua nota:" % x)))

    #Fazer a média.
    media = sum(listaNotas) / len(listaNotas)

    #executar uma interação.
    for index, value in enumerate(mediaAproveitamento):
        #fazer a verificação.
        if media <= value[1] and media  > value[0]:
            print ("Conceito:" + value[2])          
