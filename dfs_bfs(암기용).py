def DFS(L,n,k,data):
    if L == k:
        print(*data)
    else :
        for i in range(1, n+1):
            data.append(i)
            DFS(L+1, n, k, data)
            data.pop() 
L = 0
n = 3
k = 2

data = []

DFS(L,n,k, data)

from collections import deque
def BFS():
    dQ=deque()
    dQ.append(1)
    L=0
    while(dQ):# deque가 비어있을때까지
        length=len(dQ)
        for _ in range(length):
            v=dQ.popleft()
            print(v, end='')
            for nv in [v*2, v*2+1]:
                if nv> 7:
                    continue
                dQ.append(nv)
        L+=1

BFS()
