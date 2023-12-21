# platform: beecrowd - https://www.beecrowd.com.br/judge/pt/problems/view/2533
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

while True:
    try:
        courseAmount = int(input())

        dividend = 0
        divisor = 0

        for _ in range(courseAmount):
            line = list(map(int,input().split()))
            
            courseGrade = line[0]
            courseHours = line[1]
            
            dividend += courseGrade * courseHours
            divisor += courseHours
            
        result = dividend/(divisor*100)

        print("{:.4f}".format(result))

    except EOFError:
        break