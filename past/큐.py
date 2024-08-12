from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

g = deque()
for _ in range(n):
    a, *b = input().split()

    if len(b)== 1 :
        g.append(int(b[0]))
    elif a == "front":
        if len(g) == 0 :
            print(-1)
            continue
        print(g[0])
    elif a == "pop":
        if len(g) == 0 :
            print(-1)
            continue
        t = g.popleft()
        print(t)
    elif a == "size":
        # if len(g) == 0 :
        #     print(-1)
        #     continue
        print(len(g))
    elif a == "empty":
        if len(g) == 0 :
            print(1)
            continue
        print(0)
    elif a == "back":
        if len(g) == 0 :
            print(-1)
            continue
        print(g[-1])
