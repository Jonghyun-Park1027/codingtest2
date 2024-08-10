import sys
input=sys.stdin.readline
t = int(input())
for _ in range(t):
    g= list(input().strip())[::-1]
    # print(g)
    left = []
    right = []

# if g[-1]:
#     print("yes")
    while g: 
        cnt = g[-1]
        if cnt== "<": 
            if not left : 
                g.pop()
                
                continue
            else :
                g.pop()
                a = left.pop()
                right.append(a)
        elif cnt == ">" :
            if not right :
                g.pop()
                continue
            else :
                g.pop()
                a = right.pop()
                left.append(a)
        elif cnt == "-":
            if not left :
                g.pop()
                continue
            else :
                g.pop()
                left.pop()
        else :
            a = g.pop()
            left.append(a)
    # print("left:", left)
    # print("right:", right)
    left = "".join(left)
    right = "".join(right[::-1])
    print(left+right)