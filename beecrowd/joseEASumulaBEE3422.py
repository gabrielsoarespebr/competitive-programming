# platform: beecrowd - https://judge.beecrowd.com/pt/problems/view/3422
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

qtdOcorrencias = int(input())

for _ in range(qtdOcorrencias):
    minutoTempoLista = input().split()

    minuto = int(minutoTempoLista[0])

    acrescimo = 0

    if minuto > 45:
        acrescimo = minuto - 45
        if (minutoTempoLista[1] == "1T"):
            print('45+' + str(acrescimo))
        else:
            print('90+' + str(acrescimo))
    else:
        if (minutoTempoLista[1] == "1T"):
            print(str(minuto))
        else:
            print(str(minuto + 45))
