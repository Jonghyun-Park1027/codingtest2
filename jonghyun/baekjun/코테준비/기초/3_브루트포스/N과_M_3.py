n, m = map(int, input().split())
data = []
def DFS(L,n,m,data):
    if L == m:
        print(*data)
        return
    for i in range(1,n+1):
        data.append(i)
        DFS(L+1,n,m,data)
        data.pop()

DFS(0,n,m,data)