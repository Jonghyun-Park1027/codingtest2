n, m = map(int, input().split())
data = sorted(list(map(int,input().split())))

check = [0] * 10001

graph = []


start = 0

def DFS(L,n, m, data, check, graph,start):
    if L == m:
        print(*graph)
        # start += 1
        return
    for i in range(start, n):
        # if check[data[i]] == True:
            
        #     continue
        # check[data[i]]=True
        graph.append(data[i])
        # start +=1
        DFS(L +1, n, m, data, check, graph,start)
        start += 1
        graph.pop()
        # check[data[i]] = False

DFS(0, n, m, data, check, graph, start)