import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
# visit = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    # G[a].append(b)
    G[b].append(a)

# print(G)
# bfs로 푼다


def bfs(start):
    # visit = [0 for _ in range(N + 1)]
    ary = deque([start])
    # cnt = ary.pop()
    visit[start] = 1
    # n += 1
    cnt = 1
    # ary.extend(G[cnt])
    while ary:
        num = ary.popleft()
        # print(ary)
        for next_v in G[num]:
            if not visit[next_v]:
                visit[next_v] = 1
                ary.append(next_v)
                cnt += 1

    return cnt


max_cnt = 0
result = []


for i in range(1, N + 1):
    visit = [0 for _ in range(N + 1)]
    cnt = bfs(i)
    # print(cnt)
    if cnt > max_cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)

print(*sorted(result))
