#! usr/bin/env python3

##############################################################################################
#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o
#custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
#sobre vendas.
##############################################################################################


def somaImposto(taxaImposto, custo):
    #cálculo do imposto.
    resultado_imposto = custo + (custo * taxaImposto / 100)
    #retorno do resultado do imposto
    return resultado_imposto
    

somaImposto(10, 45.00)
