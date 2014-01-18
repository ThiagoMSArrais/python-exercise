#! usr/bin/env python3

#############################################################
# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.
#############################################################

def mensagemTurno():
    #Dicionário turno.
    dicionario_turno = {'M' : 'Bom Dia!', 'V' : 'Boa Tarde!', 'N' : 'Boa Noite!'}

    #recebe o valor do turno que o aluno estuda.
    turno = input("Por favor, informe o turno que você estuda:")

    #converter para uppercase
    turno = turno.upper()

    #verificar no dicionario_turno se tem o valor digitado caso tenha
    #mande mensagem com o resultado e caso nao tenha gere uma mensagem
    # de erro.
    if turno in dicionario_turno:
        print (dicionario_turno[turno])
    else:
        print ("Valor Inválido!")
        mensagemTurno()
