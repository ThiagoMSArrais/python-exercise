#! usr/bin/env python3

#########################################################################
#Faça um programa para o cálculo de uma folha de pagamento, sabendo que
#os descontos são do Imposto de Renda, que depende do salário bruto
#(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
#a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade
#de horas trabalhadas no mês.
#
#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as
#informações, dispostas conforme o exemplo abaixo. No exemplo o valor
#da hora é 5 e a quantidade de hora é 220.
#########################################################################


def calcularFolhaPagamento():
    
    #Variáveis
    sindicato = 0.0
    salarioLiquido = 0.0
    descontoIR = 0.0
    fgts = 0.0

    #solicitando valor da sua hora.
    try:
        valorHora = float(input("Informe o valor hora:"))

    except ValueError:
        print ("Por favor, informe o valor correto que ganha por hora.")
        calcularFolhaPagamento()

    #solicitando quantidade de horas e depois calcular valor hora e quantidade
    #de horas trabalhados, para saber o salário bruto.
    try:
        quantidadeHora = float(input("Por favor, informe quantidade de horas trabalhados:"))
        salarioBruto = valorHora * quantidadeHora

    except ValueError:
        print ("Valor inválido! Por favor, informe somente o valor numérico.\n")
        calcularFolhaPagamento()


    #tupla com valor maximo, minimo, desconto e valor booleano isento.
    tupla_desconto = ((900, 1, 0, True), (1500, 901, 5, False), (2500, 1501, 10, False), (2501, None, 20, False))

    for value in tupla_desconto:
        if not value[3]:
            pass
        else:
            if salarioBruto <= value[0] and salarioBruto >= value[1]:
                fgts = salarioBruto * 11 / 100
                inss = salarioBruto * 10 / 100
                sindicato = salarioBruto * 3 / 100
                totalDesconto = inss + sindicato
                salarioLiquido = salarioBruto - (sindicato + inss)
                print ("Salário Bruto: (" + str(valorHora) + " * " + str(quantidadeHora) + ") : R$" + str(salarioBruto) + "\n(-) IR (0%)   : Isento\n(-) INSS (10%)    :R$" + str(inss) + "\nFGTS(11%)    : R$" + str(fgts) + "\nTotal de descontos : R$" + str(totalDesconto) + "\nSalário Líquido : R$" + str(salarioLiquido))

calcularFolhaPagamento()
