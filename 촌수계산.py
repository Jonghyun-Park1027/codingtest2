from collections import deque

N = int(input())  # 전체 사람 수

target_1, target_2 = map(int, input().split())

M = int(input())  # 부모자식들간의 관계 개수

G = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# print(G[1:])

# answer = -1


def dfs(start, k, n):  # k 는 찾는위치 n 은 0부터 출발하여 리턴값
    # global answer
    if start == k:
        # return n
        # answer = max(answer, n)
        # print(f"start : {start}, k : {k}")
        return n

    # print(f"start : {start}, n : {n}, visit : {visit[1:]}")

    # return dfs(ary, k, n + 1)
    for i in G[start]:
        # print(f"i : {i}")
        if not visit[i]:
            visit[i] = 1
            # print(f"i : {i}")
            ans = dfs(i, k, n + 1)
            if ans:
                return ans

            # visit[i] = 0
            # visit[i] = 0

    # return -1


visit[target_1] = 1

# answer = dfs(target_1, target_2, 0)
answer = dfs(target_1, target_2, 0)
if not answer:
    answer = -1
print(answer)
