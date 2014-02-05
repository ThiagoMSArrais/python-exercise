#! usr/bin/env python3

###################################################################################################################
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro
#
# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor
# a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
#####################################################################################################################


def descontoCombustivel():
    
    #inicializar variável.
    tipo_combustivel = ""
    calculo_valor_combustivel = 0

    #dados amarzenados sobre tipo de combustível, preço, desconto até 20 litros e desconto acima de 20 litros.
    desconto = [("gasolina", 2.50, 4, 6), ("alcool", 1.90, 3, 5)]
    
    try:
        #obter quantidade de litro(s).
        litro = float(input("Por favor, informe a quantidade de litro que deseja:"))
    
    except ValueError:
        print ("Por favor, informe um valor númerico.")
        descontoCombustivel()
    
    while True:
    
        #obter tipo de combustível.
        tipo_combustivel = input("Por favor, informe o tipo de combustível desejado (Gasolina ou Álcool):")

        #verificar compatibilidade de dados obtido com os dados armazenados.
        if tipo_combustivel in desconto[0][0] or tipo_combustivel in desconto[1][0]:
            break
        
        else:
            continue
        
    #tratar dados.
    for index in range(2):
        if desconto[index][0] == tipo_combustivel:
            #verificar se o valor obtido é maior que vinte litros.
            if litro > 20:
                #efetuar o cálculo com desconto referenciado acima de vinte litros
                calculo_valor_combustivel = (litro * desconto[index][1]) - (desconto[index][1] * desconto[index][3] / 100)
                break
            
            else:
                #efetuar o cáculo com desconto referenciado abaixo de vinte litros
                calculo_valor_combustivel = (litro * desconto[index][1]) - (desconto[index][1] * desconto[index][2] / 100)
                break

    print ("Tipo de combustível:%s\nQuantidade de litro:%.1f\nTotal com desconto R$%.f\n" % (tipo_combustivel, litro, calculo_valor_combustivel))
    
