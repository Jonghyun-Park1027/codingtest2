n = int(input())

graph = [[0]*2 for _ in range(n)]

graph[0][0], graph[0][1] = 2, 2

for i in range(1, n):
    graph[i][0] = graph[i-1][0] + 2
    graph[i][1] = graph[i-1][1] + 2




print(graph)