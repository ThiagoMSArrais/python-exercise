#! usr/bin/env python3

########################################################################################################
#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.
########################################################################################################


def tratarNumeros():

    #lista de números.
    lista_numeros = []
   
    #fazer o for e obter os valores.
    for i in range(1,3):
        #obter os valores
        lista_numeros.append(input("Por favor, informe um número:"))
        
    #verificar se temos dois valores preenchidos.    
    if len(lista_numeros) == 2:
        #gerar algumas variáveis.
        par_ou_impar = ""
        positivo_ou_negativo = ""
        inteiro_ou_decimal = 0
        
        #obter o tipo de operador.
        tipo_operador = eval(input("Por favor, informe um tipo de operador:"))
        #efetuar o cálculo da lista_numeros com o tipo_operador.
        calculo_resultado = eval(lista_numeros[0]) tipo_operador eval(lista_numeros[1])
        #Verificar o calculo_resultado se é Par ou Ímpar.
        if calculo_resultado % 2 == 0:
            #armazenar o resultado Par na variável.
            par_ou_impar = "Par"
            
        else:
            #armazenar o resultado Ímpar na variável.
            par_ou_impar = "Ímpar"
            
        #verificar se o calculo_resultado é valor Positivo ou Negativo.
        if calculo_resultado >= 0:
            #armazenar o resultado Positivo na variáve.
            positivo_ou_negativo = "Positivo"
            
        else:
            #armazenar o resultado Negativo na variável.
            positivo_ou_negativo = "Negativo"
            
            
        #Verificar se o calculo_resultado é Inteiro ou Decimal.
        if isinstance(calculo_resultado, int):
            #armazenar o resultado como Inteiro na variável.
            inteiro_ou_decimal = "Inteiro"
            
        elif isinstance(calculo_resultado, float):
            #armazenar o resultado como Decimal na variável.
            inteiro_ou_decimal = "Decimal"
            
        #Imprimir as informações obtidas.
        print("Valor do resultado:" + calculo_resultado + " é %s, %s e número %s" % (par_ou_impar,\
                                                                                     positivo_ou_negativo,\
                                                                                     inteiro_ou_decimal))
            
    
