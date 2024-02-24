import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    t = input().split()
    for i in t:
        print(i[::-1], end = ' ')
    print("")