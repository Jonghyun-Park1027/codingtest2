from collections import deque

M, N, H = map(int, input().split())


graph = []
check = []
if H == 1:
    graph.append([list[int](map(int, input().split())) for _ in range(N)])
    check.append([[0] * M for _ in range(N)])
else:
    for _ in range(H):
        graph.append([list(map(int, input().split())) for _ in range(N)])
        check.append([[0] * M for _ in range(N)])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


#  1 익은거, 0 안익은거, -1 없는칸
def BFS(m, n, h, count):
    #  return 조건
    #  높이가 H와 같아졌을 때

    # 칸수를 넘어갈때
    # M과 N 끝에 도달했을 때
    need_visit = deque()
    # for i in range(N):
    #     for j in range(M):
    #         if graph[i][j]:
    #             need_visit.append([i, j])
    need_visit.append(())
    while need_visit:
        x, y = need_visit.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                need_visit.append([nx, ny])

            # if not check[H][y][x]:
            #     check[H][y][x] = True
            # DFS(M, N, H, count + 1)


# BFS()
print(graph)
print(check)
answer = 0
# for height in graph:
#     for row in height:
#         for col in row:
#             if graph[height][row][col]:
#                 BFS(col, row, height, 0)
# for height in graph:
#     for row in height:
#         for col in row:
#             if row == 0:
#                 print(-1)
#                 exit(0)
#         answer = max(answer, max(height))
# print(answer)
