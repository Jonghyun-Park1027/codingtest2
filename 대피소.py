from itertools import combinations

N, K = map(int, input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

comb = list(combinations(range(N), K))

# print(comb)
INF = float("inf")
answer = INF

for house in comb:
    case = 0
    for house_idx in range(N):
        distance = INF
        # print(house_idx)
        for hide in house:
            temp = abs(x[house_idx] - x[hide]) + abs(y[house_idx] - y[hide])
            distance = min(temp, distance)
        case = max(case, distance)
    answer = min(case, answer)
print(answer)
