#! usr/bin/env python3

########################################################################
# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
########################################################################


def lerNotas():

    # lista das notas das provas
    lista_notas = []

    for x in range(1, 3):
        lista_notas.append(float(input("%d) Infrome a sua nota:" % x)))

    media = sum(lista_notas) / len(lista_notas)

    if media >= 7 and media < 10:
        print ("Aprovado, nota:%.1f!" % media)

    elif media < 7:
        print ("Reprovado, nota:%.1f!" % media)

    elif media == 10:
        print ("Aprovado com Dinstinção")
