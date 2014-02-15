#! usr/bin/env python3

####################################################################################################
#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo
####################################################################################################


for x in range(10):
    #imprimir o titulo.
    print ("Tabuada de " + str(x+1))
    for y in range(10):
        #imprimir na tela a tabuada.
        print (str(x+1) + "x" + str(y+1) + "=" +  str((x+1)*(y+1)))
