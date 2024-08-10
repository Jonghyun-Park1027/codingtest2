# import sys
# input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

def prime(n):
    if n < 2 :
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

answer = 0

for i in a:
    answer += prime(i)
print(answer)
        
