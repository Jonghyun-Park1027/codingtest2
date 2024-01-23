# D(n) = D(n-1) + D(n-2)
import sys
#n의 범위 1<n<1000
input = sys.stdin.readline
n = int(input())

ans = [0] * 1001

ans[0] = ans[1] = 1

for i in range(2, 1001):
    ans[i]= ans[i-1] + ans[i-2]
    if i == n:
        break
print(ans[n]%10007)