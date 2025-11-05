import sys


def input():
    return sys.stdin.readline().rstrip()


left = list(input())
m = int(input())

right = []

# def cal(t, x):

for _ in range(m):
    a, *b = input().split()
    if a == "P":
        left.append(b[0])
    elif a == "L":
        if not left:
            continue
        t = left.pop()
        right.append(t)
    elif a == "B":
        if not left:
            continue
        left.pop()
    elif a == "D":
        if not right:
            continue
        t = right.pop()
        left.append(t)

    # print(a, b)
# print(left)
# print(right)
while right:
    t = right.pop()
    left.append(t)

print("".join(left))
