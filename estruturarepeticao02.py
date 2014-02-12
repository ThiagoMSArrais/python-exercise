#! usr/bin/env python3

##########################################################################################################
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.
##########################################################################################################


def obter_login():

    while True:
    
        #obter nome do usuário.
        username = input("Username:")
        
        #obter senha do usuário.
        password = input("Password:")
        
        #verificar se o username e senha, são iguais, caso sejam continuar no looping requisitando até ambos valores
        #serem distintos.
        if username == password:
            #imprimir a tela de erro e continuar o looping.
            print ("Error!")
            continue
            
        else:
            #sair do looping pelo motivo de estar correto os valores inseridos.
            break
