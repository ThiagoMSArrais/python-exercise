#! usr/bin/env python3

#############################################################
#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
##############################################################



def validar_dados():

    #dicionário para serem amarzenados os dados digitados adiante.
    dic_dados = {}
    
    #utilizando o looping para o nome
    while True:
        #obter nome.
        dic_dados['nome'] = input("Nome:")
        
        if len(dic_dados['nome']) > 3:
            #sair do looping pelo valor está correto.
            break
        
        else:
            #continuar no looping pelo motivo do valor nâo estar correto(menor que 3).
            continue
        
    #utilizando o looping para a idade.
    while True:
        
        try:
            #obter a idade entre 0 e 150.
            dic_dados['idade'] = int(input("Idade:"))
            
            #verificar se a idade está entre 0 à 150.
            if dic_dados['idade'] > 0 and dic_dados['idade'] < 150:
                #sair do looping pelo motivo de satisfazer o que foi pedido acima.
                break
            
            else:
                #Imprimir uma mensagem de erro, pelo motivo de nâo satisfazer o que foi solicitado acima.
                print ("Valor inválido!")
                continue
                
            
        except ValueError:
            #Imprimir valor de error.
            print ("Valor inválido!")
            continue
        
    #utilizando o looping para o salário      
    while True:
        
        try:
            
            #obter o valor do salário.
            dic_dados['salario'] = float(input("Salário:"))
            
            #verificar se o salário é maior do que zero.
            if dic_dados['salario'] > 0:
                #sair do looping pelo motivo de ter obtido o sucesso com o valor superior a zero.
                print ("Valor inválido!")
                break
            
            else:
                #continuar no looping pelo motivo de nâo satisfazer com o valor obtido.
                continue
            
        except ValueError:
            #imprimir na tela uma mensagem de erro, caso não tenha inserido um valor float.
            print ("Valor inválido!")
            #continuar o looping para inserir o valor corretamente.
            continue
    
    #utilizando o looping para obter o tipo de sexo.    
    while True:
        
        #obter o tipo do sexo:
        dic_dados['sexo'] = input("Sexo(F ou M):")
        
        #verificar o tipo do sexo e se está correto a informação.
        if dic_dados['sexo'].upper() in ('F', 'M'):
            #sair do looping pelo motivo de obter sucesso na informação obtida.
            break
        
        else:
            #continuar no looping para obter o valor corretamente.
            continue
    
    #utilizando o looping para o estado cívil.
    while True:
        
        #obter o valor do estado cívil.
        dic_dados['estado_civil'] = input("Estado Cívil:")
        
        #verificar o estado cívil
        if dic_dados['estado_civil'].lower() in ('s', 'c', 'v', 'd'):
            #sair do looping pelo motivo de obter o valor desejado acima.
            break
        
        else:
            #continuar o looping pelo motivo de não ter obtido o valor desejado.
            continue
        
    print ("Nome:{0}\nIdade:{1}\nSalário R${2}\nSexo:{3}\nEstado Cívil:{4}".format(dic_dados['nome'],
                                                                                   dic_dados['idade'],
                                                                                   dic_dados['salario'],
                                                                                   dic_dados['sexo'],
                                                                                   dic_dados['estado_civil'))
    
