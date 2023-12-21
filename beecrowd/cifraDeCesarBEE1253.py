# platform: beecrowd - https://www.beecrowd.com.br/judge/pt/problems/view/1253
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

testAmount = int(input())

for _ in range(testAmount):
    textEncoded = input()
    displacement = int(input())
    
    textDecodedList = []
    
    for caractereEncoded in textEncoded:
        ascIIEncoded = ord(caractereEncoded)
        ascIIDecoded = ascIIEncoded - displacement
        if ascIIDecoded < 65:
            ascIIDecoded += 26
        caractereDecoded = chr(ascIIDecoded)
        textDecodedList.append(caractereDecoded)
        
    textDecoded = ''.join(textDecodedList)
    
    print(textDecoded)