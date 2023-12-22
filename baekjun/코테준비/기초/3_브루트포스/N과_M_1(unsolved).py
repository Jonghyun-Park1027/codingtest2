N, M = map(int,input().split())
ch = [False] *(N+1)
data = [0] * M
# print(ch)
def DFS(L, N,M):
    # global ch, data
    if L == M :
        print(*data)
        return
    # else :
    for i in range(1, N+1):
        if ch[i] :
            continue
        data[L] = i
        ch[i] = True
        DFS(L+1,N, M)
        ch[i] = False
        # data.pop()
DFS(0, N, M)