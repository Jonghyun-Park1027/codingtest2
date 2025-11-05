from itertools import combinations

t = list(map(int, input().split()))
# a, b, c = t
long = max(t)
short = [i for i in t if i != long]
a, b = short
c = long
# print(short)
cnt = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            if k**2 < i**2 + j**2:
                cnt = max(cnt, i + j + k)
print(cnt)
