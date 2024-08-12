# k는 100000이하
import sys
input = sys.stdin.readline
k = int(input())

g = []

for _ in range(k):
    cnt = int(input())
    if cnt == 0:
        g.pop()
        continue

    g.append(cnt)

print(sum(g))    