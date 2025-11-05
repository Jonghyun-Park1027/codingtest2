# import sys

Computer = int(input())
N = int(input())
G = [[] for _ in range(Computer + 1)]
check = [0 for _ in range(Computer + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def bfs(ary, n):
    # ary.append(n)
    # check[n] = 1
    cnt = ary.pop()
    n += 1
    check[cnt] = 1
    ary += G[cnt]
    while ary:
        # print(n)
        cnt = ary.pop()
        if not check[cnt]:
            check[cnt] = 1
            ary += G[cnt]
            n += 1
            # ary += G[cnt]

    return n - 1
    # if not check[cnt]:
    #     bfs(ary + ary[cnt], n + 1)


print(bfs([1], 0))
