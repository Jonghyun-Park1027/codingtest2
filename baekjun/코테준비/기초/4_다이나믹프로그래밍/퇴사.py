# dynamic

n= int(input())
t = []
p = []
check = [0] * n
for _ in range(n):
    a, b = map(int,input().split())
    t.append(a)
    p.append(b)
answer = 0
def go(cnt, start):
    global answer
# target = 0
    if start > n :  
        return
    answer = max(answer, cnt)
    # cnt = 0
    for i in range(start, n):
        if i < start :
            continue
        start += t[i]
        cnt += p[i]
go(0, 0)
print(answer)
