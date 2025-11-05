import sys


# def input():
#     return sys.stdin.readline().rstrip()


n = int(input())
g = list(map(str.rstrip, sys.stdin.readlines()))
# print(g)
answer = []
left = [str(i) for i in range(n, 0, -1)]
right = []

num = 0
while True:
    if not left:
        break
    right.append(left.pop())
    answer.append("+")
    # print(f"left : {left}")
    # print(f"right : {right}")
    while True:
        # print("act")
        if not right:
            break
        if g[num] == right[-1]:
            right.pop()
            answer.append("-")
            num += 1
        else:
            break
# print(answer)
if len(right) != 0:
    print("NO")
else:
    print("\n".join(answer))
