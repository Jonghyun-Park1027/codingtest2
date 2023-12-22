n = int(input())
graph = list(map(int,input().split()))
check = [1] * n
# print(graph)
answer = [-1] * n
for i in range(n):
    cnt = 0
    for j in range(i):
        if graph[i] > graph[j] and check[j] + 1 > check[i]:
            check[i] = max(check[i], check[j]+1)
            check[i] = check[j] + 1
            # print(cnt)
            # if graph[j] > answer[-1]:
            answer[i] = j
    # for j in range(i, n):
    #     if graph[j] > answer[-1]:
    #         answer.append(graph[j])
ans = max(check)
print(ans)
p = [i for i, x in enumerate(check) if x == ans][0]
def go(p):
    if p == -1 :
        return
    go(answer[p])
    # print(p)
    print(graph[p], end= ' ')
# test = [i for i in answer if i != -1]
# print(answer)
# print(graph)
# print(p)
go(p)
# print(p)
# print(p)
# print(answer)
# print(p)
# answer = sorted(list(set(answer)))
# print(check)
# print(len(answer))
# print(*answer)

