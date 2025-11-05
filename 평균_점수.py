answer = []
for _ in range(5):
    t = int(input())
    if t <= 40:
        t = 40
    answer.append(t)

print(sum(answer) // 5)
