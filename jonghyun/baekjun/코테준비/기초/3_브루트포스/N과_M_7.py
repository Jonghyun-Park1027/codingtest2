n, m = map(int, input().split())
data = sorted(list(map(int,input().split())))

check = [0] * 10001
graph = []
start = 0
def DFS(L, m, check, graph):
    if L == m:
        print(*graph)
        return
    for i in range(len(data)):
        # if check[data[i]] == True:
        #     continue
        check[data[i]] = True
        graph.append(data[i])
        DFS(L+1, m, check, graph)
        graph.pop()
        check[data[i]] = False

DFS(0, m, check, graph)