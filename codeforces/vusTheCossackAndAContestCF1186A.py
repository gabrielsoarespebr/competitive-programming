# platform: codeforces - https://codeforces.com/problemset/problem/1186/A
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

participantAmount, penAmount, notebookAmount = map(int,input().split())

print("Yes" if penAmount >= participantAmount and notebookAmount >= participantAmount else "No")