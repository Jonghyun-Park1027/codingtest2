n = int(input())

P = list(map(int,input().split()))

# print(P)
P.sort()

for i in range(n):
    if i == 0:
        continue
    P[i] = P[i-1] + P[i]

print(sum(P)) 