import sys

# - 백스페이스, 화살표 < > ,
n = int(input())
for _ in range(n):
    left = []
    right = []
    t = sys.stdin.readline().rstrip()
    # print(t)
    for i in t:
        if i == "-":
            if not left:
                continue
            left.pop()
        elif i == "<":
            if not left:
                continue
            right.append(left.pop())
        elif i == ">":
            if not right:
                continue
            left.append(right.pop())
        else:
            left.append(i)
    while right:
        left.append(right.pop())
    print("".join(left))
