import heapq
import sys


# 배열에 자연수 x를 넣고
# 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
# 프로그램은 처음 비어있는 배열에서 시작
# def input():
#     return sys.stdin.readline().rstrip()
input = sys.stdin.readline

n = int(input())  # n<=100000
h = []
# heapq.heapify(h)
# h
for _ in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(h, num)
    else:
        if len(h) == 0:
            print(0)
            continue
        print(heapq.heappop(h))
