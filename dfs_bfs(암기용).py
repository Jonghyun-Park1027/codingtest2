def DFS(L, n, k, data):
    if L == k :
        print(*data)
        return
    for i in range(n):


        data.append(i)
        DFS(L+1, n, k, data)
        data.pop()
from collections import deque
def BFS():
    dQ= deque()
    dQ.append(1)
    L = 0
    while(dQ): # deque이 빌때까지
        length= len(dQ)
        for _ in range(len(length)):
            v = dQ.popleft()
            for nv in [v*2, v*2+1]:
                if nv > 7:
                    continue
                dQ.append(nv)

        L += 1
BFS()

