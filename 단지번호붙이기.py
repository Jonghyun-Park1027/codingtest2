from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())

graph = [list(map(int, list(input()))) for _ in range(n)]
# check = [[0] * n for _ in range(n)]
# print(graph)
# print(check)


def BFS(graph, a, b):
    # visit = []
    n = len(graph)
    need_visit = deque()
    need_visit.append((a, b))
    graph[a][b] = 0
    count = 1
    while need_visit:
        nx, ny = need_visit.pop()

        for i in range(4):
            # 상하좌우
            x = nx + dx[i]
            y = ny + dy[i]
            # 넘어가면 취소처리
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            # need_visit.append((x, y))
            # check[x][y] = True
            if graph[x][y]:
                graph[x][y] = 0
                need_visit.append((x, y))
                count += 1
    return count


cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            cnt.append(BFS(graph, i, j))
cnt.sort()
print(len(cnt))
print(*cnt, sep="\n")

# if graph[i][j] == 0 and check[i][j] == True :
# return
# 루프의 끝에서 count +=1
