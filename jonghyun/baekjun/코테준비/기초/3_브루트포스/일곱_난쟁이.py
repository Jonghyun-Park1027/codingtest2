
# 반동작 : for문이 돌아가는 대상 data에서 리스트를 제거하는 것은 위험함
data = []
for _ in range(9):
    data.append(int(input()))

answer = sum(data)
one = 0
two = 0
for i in data:
    for j in data:
        if j != i and answer -(i+j)== 100:
            one = i
            two = j
            break
data.remove(one)
data.remove(two)
data.sort()
for i in data:
    print(i)

'''
다른풀이
import sys
n = 9
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(0, n):
    for j in range(i+1, n):
        total = 0
        for k in range(0, n):
            if i == k or j == k:
                continue
            total += a[k]
        if total == 100:
            for k in range(0, n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)'''