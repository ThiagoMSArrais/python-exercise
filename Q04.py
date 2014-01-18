#! usr/bin/env python3

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def verificarLetra():

    # lista vogais
    vogal = ['a', 'e', 'i', 'o', 'u']
    
    # lista consoantes
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'k', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'y']

    letra = input("Informe uma letra:")

    if letra.lower() in vogal:
        print ("Letra %s é uma vogal!" % letra.upper())

    elif letra.lower() in consoantes:
        print ("Letra %s é um consoante!" % letra.upper())

    else:
        print ("Por favor, informe somente uma letra!")
        verificarLetra()
