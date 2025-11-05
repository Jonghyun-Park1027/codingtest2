import heapq
import sys

input = sys.stdin.readline
n = int(input())
g = []
for _ in range(n):
    cnt = int(input())
    if cnt != 0:
        heapq.heappush(g, -cnt)
    elif not g:
        print(0)
        continue
    else:
        print(-heapq.heappop(g))
    # print(cnt)
