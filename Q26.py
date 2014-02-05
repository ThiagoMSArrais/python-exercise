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

    #dados amarzenados sobre tipo de combustível, preço, desconto até 20 litros e desconto acima de 20 litros.
    desconto = [("gasolina", 2.50, 4, 6), ("alcool", 1.90, 3, 5)]
    
    try:
        #obter quantidade de litro(s).
        litro = float(input("Por favor, informe a quantidade de litro que deseja:"))
    
    except ValueError:
        print ("Por favor, informe um valor númerico.")
        descontoCombustivel()
    
    #obter tipo de combustível.
    tipo_combustivel = input("Por favor, informe o tipo de combustível desejado (Gasolina ou Álcool):")
    
    
