import sys
# input = sys.stdin.readline
t = int(input())
for _ in range(t):

    data = []
    left = []
    right = []
    a = input()

    for i in a:
        data.append(i)
        if i == ')':

            if len(data) >= 2 and data[-2] == '(':
                data.pop()
                data.pop()

    if data :
        print("NO")
    else :
        print("YES")