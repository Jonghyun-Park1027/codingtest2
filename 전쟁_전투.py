# 상하좌우용
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())  # N 가로, M 세로로
G = []
check = [[0] * N for _ in range(M)]
for i in range(M):
    G.append(input())

# print(G)
# print(check)
me = 0
enemy = 0


def bfs(t, x, y):  # t == W or t == B
    global temp
    if check[y][x]:
        return
    # if G[y][x] == t:
    #     # print(n)
    #     temp += 1
    #     return
    check[y][x] = 1
    temp += 1
    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y
        if (
            nx >= 0
            and nx < N
            and ny >= 0
            and ny < M
            and not check[ny][nx]
            and G[ny][nx] == t
        ):
            # check[ny][nx] = 1
            bfs(t, nx, ny)
            # check[ny][nx] = 0

    # return n


for y in range(M):

    for x in range(N):
        if not check[y][x]:
            temp = 0
            # check[y][x] = 1
            bfs(G[y][x], x, y)
            # print(temp)
            if G[y][x] == "W":
                me += temp**2
            else:
                enemy += temp**2
            # bfs("B", x, y)
    # print(check)
print(me, enemy)
