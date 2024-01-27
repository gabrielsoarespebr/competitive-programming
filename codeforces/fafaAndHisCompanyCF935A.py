# platform: codeforces - https://codeforces.com/problemset/problem/935/A
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

employeeAmount = int(input())

wayAmount = 1

for leaderAmount in range(2,(employeeAmount//2 + 1)):
    if ((employeeAmount-leaderAmount)%leaderAmount == 0):
        wayAmount += 1

print(wayAmount)