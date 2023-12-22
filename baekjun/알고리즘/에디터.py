import sys

left = list(sys.stdin.readline().strip())
cnt = len(left)

right = []
n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'L':
        if cnt == 0 :
            continue
        else : 
            
            cnt -= 1
            
            right.append(left.pop())
            
    elif a[0] == 'D':
        if cnt == len(left)+len(right):
            continue
        else :
            cnt += 1
            left.append(right.pop())
    elif a[0] == 'B':
        if cnt == 0:
            continue
        else :
            left.pop()
            cnt -= 1
            
    else :
        left.append(a[1])
        cnt += 1
while left :
    right.append(left.pop())

print(''.join(right[::-1]))