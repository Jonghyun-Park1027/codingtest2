import sys
input = sys.stdin.readline
k = int(input())

answer = []
for _ in range(k):
    n = int(input())
    if n == 0:
        answer.pop()
        continue
    
    answer.append(n)

print(sum(answer))
