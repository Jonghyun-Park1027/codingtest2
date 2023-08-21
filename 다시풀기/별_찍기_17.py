n = int(input())
# print("*")
max_len = n
graph = [[" "]* n]
for i in range(0, n, -1):
    graph = [[" "]* n]
    if i == n :
        graph[i] = "*"
        print("".join(graph))
    elif i != n and i != 0:
        graph[i] = "*"
        print("".join(graph)+"".join(graph[::-1]))
    else :
        print(["*"]*n*2)
    print(i)