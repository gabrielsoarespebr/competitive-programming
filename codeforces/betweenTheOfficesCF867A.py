# platform: codeforces - https://codeforces.com/problemset/problem/867/A
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

dayAmount = input()

text = input()

travelToSanFrancisco = text.count("SF")

travelToSeattle = text.count("FS")

print('YES' if travelToSanFrancisco > travelToSeattle else 'NO')