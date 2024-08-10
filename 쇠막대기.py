import sys
input = sys.stdin.readline

bar = input()
# print(bar)

n = len(bar)

stack = []
# 막대기 그래프
g = [0] * n

answer = 0
cnt = 0
for i in range(n) :
    c = bar[i]
    if c == "(":
        # cnt += 1
        # g[i]+=cnt
        stack.append(i)
    else :
        if not stack :
            continue
        if stack[-1] + 1 == i :
            stack.pop()
            answer += len(stack)
        else :
            stack.pop()
            answer += 1
    # print(cnt)
# print(g)
print(answer)