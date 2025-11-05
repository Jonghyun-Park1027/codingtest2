import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, (input().split()))

G = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v1].sort()
    G[v2].append(v1)
    G[v2].sort()


# print(G)


def DFS(v):
    # if not ary:
    #     return
    # cnt = ary.popleft()
    visit[v] = 1
    for i in G[v]:
        if visit[i] == 0:
            # ary.extend(G[v])
            visit[i] = 1
            answer.append(i)
            DFS(i)


def BFS(v):
    # visit[v] = 1
    # answer.extend(G[v])
    while v:
        cnt = v.popleft()
        # print(cnt)
        # print(cnt)
        if not visit[cnt]:
            visit[cnt] = 1
            v.extend(G[cnt])
            # print(v)
            answer.append(cnt)
        # print(answer)


# print(V, sep=" ")
# visit[V] = 1
answer = [V]
DFS(V)

print(*answer)
visit = [0 for _ in range(N + 1)]
answer = []
# visit[V] = 1
# for i in G:
#     i.sort(reverse=True)
BFS(deque([V]))
print(*answer)
# print(deque(G[V]))
# deque().
