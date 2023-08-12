''' 시간초과
t = int(input())
for _ in range(t):
    n = int(input())
    # std_n = int(n**0.5)
    sum = 0
    # data = []
    for i in range(1,n+1):
        sum += n//i*i
        # print(i, n, sum)
        # sum += (n/i)//i*i
        # if n% i == 0:
            # sum += (n/i)//i*i
        # if n % i == 0:
            # data.append(n/i)
    # for j in data :
        # sum += n//j*j
    print(sum)'''

MAX = 1000000;
d = [1]*(MAX+1)
s = [0]*(MAX+1)
for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        d[i*j] += i
        j += 1
for i in range(1, MAX+1):
    s[i] = s[i-1] + d[i]
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(s[n])
print('\n'.join(map(str,ans))+'\n')