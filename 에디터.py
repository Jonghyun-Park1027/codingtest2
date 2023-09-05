import sys
# t = sys.stdin.readline().split()
left = sys.stdin.readline().split()
cnt = len(left)
cursor = [i for i in range(cnt+1)]
# idx = 0
# if cursor[idx] == 0: # L,B 무시의 경우
    # pass
# if cursor[idx] == len(left): # D 무시의 경우
    # pass
right = []
n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'L':
        if cnt == 0 :
            continue
        else : 
            cnt -= 1
    elif a[0] == 'D':
        if cnt == len(left):
            continue
        else :
            cnt += 1
    elif a[0] == 'B':
        if cnt == 0:
            continue
        else :
            # print(cnt)
            while cnt- 1 > len(left):
                
                target = left.pop()
                print(target)
                right.append(target)
                cnt -= 1
    else :
        left.insert(cnt,a[1])
        cnt += 1
print(''.join(left))