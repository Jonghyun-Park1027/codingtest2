from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(n, m, graph):

    need_visit = deque([(0, 0)])

    # need_visit.append([0, 0])

    while need_visit:
        x, y = need_visit.popleft()

        for i in range(4):
            # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                need_visit.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(n, m, graph))
