# n = int(input())
# graph = [list(map(int,input().split())) for _ in range(n)]


# s_t = []
# l_t = []
# check = [0]*(n)
# answer = 10000
# # i 행을 +1 하면서 구함
# # j 열을 +1 하면서 구함
# def go(L,s_t, l_t, check):
# # L 이 n이 될떄 return
#     global answer
#     if L == n-1:
#         answer = min(answer, sum(s_t)-sum(l_t))
#         return
# # if not n :
# #     continue 또는 다른 방식으로 0 일때 캔슬해야함
#     for i in range(n):
#         if graph[L][i] == 0:
#             continue
#         if check[i] :
#             continue
#         if L == n/2 :
#             l_t.append(graph[i][L])
#             check[i] = True
#             l_t.append(graph[L][i])
#             check[L] = True
#             go(L+1, s_t, l_t, check)
#             l_t.pop()
#             check[i] = False
#             l_t.pop()
#             check[L] = False
# # i는 행, j는 열, 0은 자기자신
#         else :
#             s_t.append(graph[i][L])
#             check[i] = True
#             s_t.append(graph[L][i])
#             check[L] = True
#             go(L+1, s_t, l_t, check)
#             s_t.pop()
#             check[i] = False
#             s_t.pop()
#             check[L] = False

# go(0, s_t, l_t, check)
# print(answer)

def go(index, first, second):
    if index == n:
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff
    if len(first) > n//2:
        return -1
    if len(second) > n//2:
        return -1
    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
print(go(0, [], []))
