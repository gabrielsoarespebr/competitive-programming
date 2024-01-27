# platform: codeforces - https://codeforces.com/problemset/problem/1220/A
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

letterAmount = input()

text = input()

zeroAmount = text.count("z")

oneAmount = text.count("n")

binaryNumberList = oneAmount * ['1'] + zeroAmount * ['0']

binaryNumber = ' '.join(binaryNumberList)

print(binaryNumber)