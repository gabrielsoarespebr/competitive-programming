# platform: beecrowd - https://www.beecrowd.com.br/judge/pt/problems/view/3257
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

treeAmount = int(input())

growthDaysList = list(map(int,input().split()))

growthDaysList.sort(reverse=True)

maxGrowthDays = 0

# note: why did increment start with 2?
# 2 = 1 + 1
# first 1 fix the index of a list that starts at 0, to represent days: day 1, day 2...
# second 1 represents day after
increment = 2

for treeGrowthDays in growthDaysList:
    if (treeGrowthDays + increment)> maxGrowthDays:
        maxGrowthDays = treeGrowthDays + increment
    increment+=1
    
print(maxGrowthDays)