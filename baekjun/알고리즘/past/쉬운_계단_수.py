n = int(input())

d = [[0]* 10 for _ in range(101)]
for i in range(10):
    d[0][i] = i
for i in range(1,n+1):
    