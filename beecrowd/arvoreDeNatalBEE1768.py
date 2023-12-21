# platform: beecrowd - https://www.beecrowd.com.br/judge/pt/problems/view/1768
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

import math

# note: EOF structure
while True:
    try:
        treeMaxAsteriskAmount= int(input())
        
        spaceAmount = math.floor(treeMaxAsteriskAmount/2)
        
        treeTrunk = (" " * spaceAmount) + "*" + "\n" + (" " * (spaceAmount-1)) + "***" + "\n"
        
        asteriskAmount = 1
        while asteriskAmount <= treeMaxAsteriskAmount:
            print(" " * spaceAmount + "*" * asteriskAmount)
            asteriskAmount += 2
            spaceAmount -= 1
        print(treeTrunk)
    except EOFError:
        break