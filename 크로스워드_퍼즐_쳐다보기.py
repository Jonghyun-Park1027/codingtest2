R, C = map(int, input().split())

G = []

for i in range(R):
    s = list(input())
    G.append(s)
    # print(s)

# print(G)

check = [[0] * C] * R
# print(check)

# def cal(s, i, j):
#     if
answer = []
for i in range(R):
    s = ""
    for j in range(C):
        if G[i][j] == "#":
            answer.append(s)
            s = ""
            continue
        else:
            s = s + G[i][j]
    if s:
        answer.append(s)
for i in range(C):
    s = ""
    for j in range(R):
        if G[j][i] == "#":
            answer.append(s)
            s = ""
            continue
        else:
            s = s + G[j][i]
    if s:
        answer.append(s)
# print(sorted(set(answer)))
answer = [i for i in answer if len(i) >= 2]
print(sorted(answer)[0])
