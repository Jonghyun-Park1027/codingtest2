import heapq
import sys

input = sys.stdin.readline

n = int(input())
g = []
absg = []
for _ in range(n):
    cnt = int(input())
    if cnt == 0:
        if not g:
            print(0)
            continue
        else:
            print(heapq.heappop(g)[1])
    else:
        heapq.heappush(g, [abs(cnt), cnt])
