import sys
t = int(input())
input = sys.stdin.readline
for _ in range(t):
    g = input().split()
    for i in g:
        print(i[::-1], end=' ')
    print('')