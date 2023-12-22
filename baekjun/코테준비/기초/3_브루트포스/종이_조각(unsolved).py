n, m = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]

ans = 0
for s in range(1<<(n*m)):
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i * m + j
            if (s&(1<<k)) == 0:
                cur = cur * 10 + graph[i][j]
            else :
                sum += cur
                cur = 0
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            if (s&(1<<k)) != 0:
                cur = cur * 10 + graph[i][j]
            else :
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)
# def row(n,m):
#     answer = 0
#     # print()
#     for i in range(n):
#         cnt = ''
#         for j in range(m):

#             cnt += graph[i][j]
#         cnt = int(cnt)
#         # print(cnt)
#         answer += cnt
#     return answer

# def col(m,n):
#     answer = 0
#     # print()
#     for i in range(m):
#         cnt = ''
#         for j in range(n):

#             cnt += graph[j][i]
#         cnt = int(cnt)
#         # print(cnt)
#         answer += cnt
#     return answer

# t1 = row(n,m)
# # print(t1)
# t2 = col(m,n)
# # print(t2)
# answer = max(t1,t2)
# print(answer)
        