n = int(input())
answer = [0] * (n+1)
for i in range(1, n+1):
    answer[i] = i
    j = 1
    while j*j <= i:
        if answer[i] > answer[i-j*j] + 1:
            answer[i] = answer[i-j*j] + 1
        j += 1
print(answer[n])