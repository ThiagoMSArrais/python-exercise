#! usr/bin/env python3

###################################################################################
#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
#carne da promoção, porém não há limites para a quantidade de carne por cliente.
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
#sobre o total a compra. Escreva um programa que peça o tipo e a quantidade de carne
#comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
#tipo e quantidade de carne, preço total, tipo de pagamento,
#valor do desconto e valor a pagar.
####################################################################################


def fazer_pedido():

    #variável
    count = 0
    total_preco = 0.0
    tipo_carne = ""
    preco_desconto = 0.0

    #dados do produto
    dados_produto = [("file duplo", 4.90, 5.80), ("alcatra", 5.90, 6.80), ("picanha", 6.90, 7.80)]
    
    while True:
        #varial finalizar do tipo booleano para 
        finalizar = False

        #obter o tipo de carne.
        tipo_carne = input("Por favor, informe o tipo de carne que deseja:")
        
        for index in range(len(dados_produto)):
            #verificar se foi escolhiado a carne que estã na lista corretamente.
            if tipo_carne.lower() in dados_produto[index][0]:
                count = index
                finalizar = True
                break
        
        else:
            #Imprimindo na tela "valor invalido!".
            print ("Valor inválido!")
        
        if finalizar:
            break

        else:
            continue

    while True:

        try:
            #obter o valor do peso da carne.
            peso = float(input("Peso:"))

        except ValueError:
            print ("Valor invalido!")
            continue

        #verifica o peso e ver qual tipo de valor a ser calculado.
        if peso <= 5 and peso > 0:
            #calculo com valor ate de 5kg.
            total_preco = (peso * dados_produto[count][1])

        elif peso > 5:
            #calculo com valor acima de 5kg.
            total_preco = (peso * dados_produto[count][2]
            
        #obter informacao se vai ser pago no cartao tabajara.
        tipo_pagamento = input("Pagar com cartão Tabajara?:")

        #verificar se o cliente tem o cartao tabajara.
        if tipo_pagamento.lower() == 'sim':
            titulo_pagamento = "Cartao Tabajara"
            total_preco = total_preco * 5 / 100

    else:
       titulo_pagamento = "Dinheiro"

    print ("\t\t\tNota Fiscal\n\tTipo:%s\n\tQuantidade:%.3fkg\n\tPreço Total:R$%.2f\n\tTipo Pagamento:%s\n\tValor a pagar:R$%.2f\n" % (tipo_carne, peso, total_preco, titulo_pagamento, total_preco))


fazer_pedido()
