# answer 초기화


n = int(input())
graph = list(map(int,input().split()))
# graph.sort()
answer = [1]*n
# print(answer)
# print(graph)

# check = []
# print(graph)
# for문으로 list 돌기
for i in range(n):
    # cnt = graph[i]  
    # answer[i] += 1
    # print(i)
    for j in range( i,-1, -1):
        # print("j: ", j)
        if graph[i] > graph[j]:
            cnt = answer[j] + 1
            # print("i :", i)
            # print("graph[i] :", graph[i])
            # print("j :", j)
            # print("graph[j] :", graph[j])
            # print("cnt:",cnt)
            answer[i] = max(answer[i], cnt)

    # if answer[-1] < cnt:
        # answer.append(cnt)
    # elif answer[-1] > cnt:
    #     answer = [cnt]
# for i in range(0,-1,-1):
#     print(i)
print(max(answer))
# print(len(answer))
