g = list(map(int, input().split()))

answer = 0
for i in g:
    answer += i**2
print(answer%10)