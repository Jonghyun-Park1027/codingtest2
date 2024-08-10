from collections import deque

circle, n = map(int, input().split())

circle = deque([i for i in range(1, circle+1)])

answer = []
while circle:
    circle.rotate(-(n-1))
    t = circle.popleft()
    answer.append(t)

print("<", end= "")
print(*answer, sep= ", ", end = "")
print(">")