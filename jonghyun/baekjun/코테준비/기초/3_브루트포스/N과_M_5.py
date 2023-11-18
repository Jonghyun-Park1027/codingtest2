n, m = map(int, input().split())
graph = sorted(map(int,input().split()))
data = []
check = [0] * 10001
# print(graph)

def DFS(L, data, m, graph, check):
    if L == m:
        print(*data)
        return
    for i in graph:
        if check[i]:
            continue
        check[i] = True
        data.append(i)
        DFS(L+1, data, m, graph, check)
        data.pop()
        check[i] = False

DFS(0, data, m, graph, check)