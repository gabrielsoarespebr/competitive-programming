# platform: beecrowd - https://www.beecrowd.com.br/judge/pt/problems/view/1805
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

# note: arithmetic progression/sequence
line = list(map(int,input().split()))

firstNumber = line[0]
lastNumber = line[1]

numberAmount = lastNumber - firstNumber + 1

sumArithmeticProgression = int((firstNumber + lastNumber) * (numberAmount/2))

print(sumArithmeticProgression)