import sys
input = sys.stdin.readline
def cal(n):
    if n <= 3 :
        return n
    else :
        a, b = 2, 3
        for i in range(4, n+1):
            a, b = b, (a + b) % 15746
        return b

n = int(input())
print(cal(n))