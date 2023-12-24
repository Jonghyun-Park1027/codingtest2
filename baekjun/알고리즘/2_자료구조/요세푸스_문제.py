from collections import deque

n, k = map(int, input().split())

man = deque([i for i in range(1,n+1)])
k -=1

answer = []
while man :
    man.rotate(-k)
    a = man.popleft()
    answer.append(a)
print('<'+', '.join(map(str,answer))+'>')

