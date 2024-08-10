import sys
input = sys.stdin.readline
n = int(input())

stack = []

for _ in range(n):
    a, *b = input().split()
    if b:
        
        stack.append(int(b[0]))
    else :
        if a == "pop":
            if not stack :
                print(-1)
            else :
                cnt = stack.pop()
                print(cnt)
        elif a == "size" :
            print(len(stack))
        elif a == "empty":
            if stack :
                print(0)
            else :
                print(1)
        else :
            if stack :
                print(stack[-1])
            else :
                print(-1)