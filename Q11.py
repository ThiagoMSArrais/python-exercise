#! usr/bin/env python3
###################################################################################################
#As Organizações Tabajara resolveram dar um aumento de salário aos
#seus colaboradores e lhe contraram para desenvolver o programa que
#calculará os reajustes.
#
#    Faça um programa que recebe o salário de um colaborador e o 
#    reajuste segundo o seguinte critério, baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.
####################################################################################################


def reajusteSalario(salario_colaborador=0.0, percentual=0):
    valor_aumento = salario_colaborador * percentual / 100
    novo_salario = salario_colaborador + valor_aumento
    return "Salario anterior: R$%.2f\nPercentual: %d\nValor aumento: R$%.2f\nNovo salario:R$%.2f" % (salario_colaborador, percentual, valor_aumento, novo_salario)


def calcularReajuste():

    #tupla com informacoes dos valores maximo, minimo, percentual e valor boolean
    #para saber qual a condicao utilizar.
    reajustar = ((280, 0, 20, False), (700, 280, 15, False), (1500, 700, 10, False), (1500, 0, 5, True))

   
    #receber salario do colaborador.
    salario_colaborador = float(input("Informe o seu salario:"))


    for value in reajustar:
        if not value[3]:
            if salario_colaborador <= value[0] and salario_colaborador > value[1]:
                print(reajusteSalario(salario_colaborador, percentual=value[2]))
                

        else:
            if salario_colaborador > value[0]:
                print(reajusteSalario(salario_colaborador, percentual=[2])


