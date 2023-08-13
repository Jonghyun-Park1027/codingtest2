'''
unsolved : 배열 만드는것은 구현했는데 합계를 구현하는 방식을 몰라서 못품
MAX = 1000001
check = [0] * MAX
check[0] = check[1] = True

for i in range(2,MAX):
    if not check[i]:
        j = i+i
        while j < MAX :
            check[j]= True
            j += i

try :
    while True:
        q = int(input())
        data = []
        for i in range(q, 3, -1):
            if check[i] :
                data.append(i)
                print(sum(data))
    # for i in 
        

except :
    exit()
'''

# 강의내용 - input으로 받으면 시간초과됨
import sys
MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] =True
prime = []
for i in range(2, MAX+1):
    if not check[i]:
        prime.append(i)
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i
prime = prime[1:]
while True :
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for p in prime:
        if check[n-p] == False: # n-p가 소수가 아닐때
            print(f"{n} = {p} + {n-p}")
            break
'''MAX = 1000000
check = [0]*(MAX+1)
check[0] = check[1] =True
prime = []
for i in range(2, MAX+1):
    if not check[i]:
        prime.append(i)
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i
prime = prime[1:]
while 1:
    k = int(input())
    if not k:
        break
    for i in range(3, int(k / 2) + 1, 2):
        if not check[i] and not check[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")'''
'''
다른풀이
import sys


n = 1000001
# 소수 아닌 모든 홀수 처리
table = [1] * n
for i in range(3, int(n ** 0.5) + 1, 2):
    if table[i]:
        for j in range(i * 2, n, i):
            table[j] = 0
# k가 만들어지는 두 홀수인 소수 검색
while 1:
    k = int(sys.stdin.readline())
    if not k:
        break
    for i in range(3, int(k / 2) + 1, 2):
        if table[i] and table[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")'''