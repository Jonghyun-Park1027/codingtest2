# 상하좌우
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def RGB(graph, visited, x, y, n):
    # visit = []
    color = graph[x][y]
    need_visit = deque([(x, y)])
    visited[x][y] = True
    while need_visit:

        x, y = need_visit.popleft()

        # 상하좌우 검사
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and graph[nx][ny] == color
            ):
                visited[nx][ny] = True
                need_visit.append((nx, ny))


n = int(input())

graph = [list(input()) for _ in range(n)]

RGB_picture = [[False] * n for _ in range(n)]
RB_picture = [[False] * n for _ in range(n)]

count_normal = 0

for i in range(n):
    for j in range(n):
        if not RGB_picture[i][j]:
            RGB(graph, RGB_picture, i, j, n)
            count_normal += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"
count_rg_blind = 0

for i in range(n):
    for j in range(n):
        if not RB_picture[i][j]:
            RGB(graph, RB_picture, i, j, n)
            count_rg_blind += 1


# RGB(graph, n)

print(count_normal, count_rg_blind)
