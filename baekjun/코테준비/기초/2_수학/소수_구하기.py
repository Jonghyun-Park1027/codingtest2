m,n = map(int, input().split())
MAX = 1000000
check = [0 for i in range(MAX+1)]
graph = [i for i in range(MAX+1)]
check[0] = check[1] = 1
# print(graph)
# print(graph)
for i in graph:
    # print(i)
    if not check[i] and i*i < MAX:
        # print(i)
        num = i
        while i+num < MAX :
            i += num
            check[i] = 1
            # print(i)
    # print(i)
            
for i in range(m, n+1):
    if not check[i] :
        print(graph[i])