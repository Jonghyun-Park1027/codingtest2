# 먼저 에라토스테네스의 체를 만들어야함
import sys
input = sys.stdin.readline
MAX = 1000001
check = [0] * MAX

# 소수면 check[i] = 1
#prime 배열을 만든다
prime= []

for i, v in enumerate(check):
    if i == 0 or i == 1:
        continue

    if v == 0:
        prime.append(i)
        c= i
        c += i
        # print(check[:100])
        while c < MAX:
            if check[c] != 1:
                check[c] = 1
            c += i
check[0] = check[1] = 1
# print(prime)
# print(check[:100])
while True :
    n = int(input())
    if n == 0:
        exit(0)
    for i in prime:
        
        if check[i] == 0 and check[n-i] == 0:
            print(f"{n} = {i} + {n-i}")
            break