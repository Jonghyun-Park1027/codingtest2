import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    empty = 0
    if len(stack)== 0 :
        empty = -1
    # [pu, po, si, em, to]
    act = list(sys.stdin.readline().split())
    if act[0] == "push":
        stack.append(act[1])
    elif act[0] == "pop":
        if empty == -1:
            print(empty)
        else : 
            a = stack.pop()
            print(a)
    elif act[0] == "size":
        print(len(stack))
    elif act[0] == "empty":
        if empty == -1:
            print(1)
        else :
            print(0)
    elif act[0]== "top":
        if empty == -1:
            print(-1)
        else :    
            print(stack[-1])

