# xy 좌표를 변경하는 조건 필요함
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(ary, x, y):
    # if cab[y][x] != 1 or visit[y][x]:
    #     return
    # for i in range(4):
    #     nx = x + dx[i]
    #     ny = y + dy[i]
    #     if nx < 0 or nx >= M or ny < 0 or ny >= N:
    #         continue
    #     else:
    #         visit[y][x] = 1
    #         bfs(nx, ny)

    visit[y][x] = 1
    ary.append((x, y))
    while ary:
        x, y = ary.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            else:
                if visit[ny][nx] == 0 and cab[ny][nx]:
                    visit[ny][nx] = 1
                    ary.append((nx, ny))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    cab = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        cab[b][a] = 1
        # print(a, b)
    # print(cab)

    # bfs 사용

    answer = 0
    for x in range(M):
        for y in range(N):

            # and 조건을 통해 배추(1)이고, visit(0)일 경우를 순회
            if cab[y][x] == 1 and visit[y][x] == 0:
                bfs([], x, y)
                answer += 1
    print(answer)
    # print(cab)
# 배추 심어진 곳을 한번 돌고 나올때마다 count += 1
