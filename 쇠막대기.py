num = 0
answer = 0
pipe = input()
left = []
right = []
for i in range(len(pipe)):
    if pipe[i] == "(":
        # left.append(pipe[i])
        # answer += 1
        num += 1
    else:  # 닫는괄호일때
        if pipe[i - 1] == ")":  # 이전 괄호도 )였다면 그냥 닫는괄호임
            num -= 1
            answer += 1
        else:
            num -= 1
            # left.pop()
            answer += num
print(answer)
