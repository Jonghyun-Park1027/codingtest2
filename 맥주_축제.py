import sys
import heapq
from itertools import permutations, combinations

input = sys.stdin.readline
n, m, k = map(int, input().split())  # n 파티개최일수, m 채워야할 만족도값, k 맥주종류류


beers = []
for _ in range(k):
    cnt = list(map(int, input().split()))
    beers.append(cnt)


beers.sort()

answer = float("inf")
heap = []
total_happy = 0
# happy = 0
for alchol, happy in beers:
    heapq.heappush(heap, happy)
    total_happy += happy
    # print(alchol, happy)
    # heap에 더하다가 n보다 작아진거같으면 만족도가 낮은 술을 빼준다.
    if len(heap) > n:
        total_happy -= heapq.heappop(heap)
    if len(heap) == n and total_happy >= m:
        # 파티 개최일 3일을 맞췄는데, 만족도가 기준치 이상이 될 경우
        answer = max(heap)

        # print(party)
        break
# print(heap)
if answer == float("inf"):
    print("-1")
else:
    print(answer)
