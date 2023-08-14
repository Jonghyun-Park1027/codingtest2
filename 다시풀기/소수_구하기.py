MAX = 1000001
check = [0]*MAX
check[0] = check[1] = 1
n, m = map(int,input().split())
for i in range(2,MAX):
    if check[i] == 0:
        # print(i)
        j = i+i
        while j<MAX:
            check[j] = 1
            j += i
for i in range(n,m+1):
    if check[i] ==0:
        print(i)