import sys
from collections import Counter

n = int(input())  # 주의 수
g = Counter()
readline = sys.stdin.readline

for i in range(n):
    for j in range(4):  # 한 달에 4주
        s = readline().split()
        if j == 0:
            add = 4
        elif j == 1:
            add = 6
        elif j == 2:
            add = 4
        elif j == 3:
            add = 10
        for k in range(7):  # 한 주에 7일
            if s[k] != "-":
                g[s[k]] += add

# Counter가 비어 있는 경우(모든 값이 "-") 대비
if not g:
    print("Yes")
else:
    answer = max(g.values()) - min(g.values())
    print("No" if answer > 12 else "Yes")
