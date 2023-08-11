n = int(input())
for _ in range(n):
    stack = []
    answer = []
    data = input()
    for i in data:
        if i != ' ':
            stack.append(i)
        else :
            for i in stack:
                stack.pop(i)
