n, m = map(int,input().split())
data = []
start = 1
def DFS(L, n, m, start):
    if L == m :
        print(*data)
        return
    for i in range(start, n+1):
        data.append(i)
        DFS(L+1, n, m, i)
        data.pop()

DFS(0, n, m, start)
