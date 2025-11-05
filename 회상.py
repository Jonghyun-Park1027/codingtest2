from collections import Counter


N, M = map(int, input().split())
# N : 수업의 개수 M : N중에 몇개의 수업을 들었는지 선택할 숫자
# print(N)
g = Counter()
for _ in range(N):
    I = int(input())
    # print(I)
    k = input().split()
    for j in range(I):
        g[k[j]] += 1
if not g:
    print(0)
else:
    print(len([i for i in g.values() if i >= M]))
