stack = []
n = int(input())
for _ in range(n):
    empty = 0
    if len(stack)== 0 :
        empty = -1
    # [pu, po, si, em, to]
    act = list(input().split())
    if act[0][:2] == "pu":
        stack.append(act[1])
    elif act[0][:2] == "po":
        if empty == -1:
            print(empty)
        