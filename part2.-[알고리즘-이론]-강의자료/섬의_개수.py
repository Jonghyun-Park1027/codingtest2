import sys
sys.setrecursionlimit(10000)

# 방향 벡터 (상, 하, 좌, 우, 대각선 방향들)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y, grid, visited, h, w):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                dfs(nx, ny, grid, visited, h, w)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))
    
    visited = [[False] * w for _ in range(h)]
    island_count = 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, grid, visited, h, w)
                island_count += 1
    
    print(island_count)
