'''
unsolved : 구현실패, 시간초과(30분)
n = int(input())

count =1
answer = 0
while True:
    target = count* 10

    n -=  10
    if n <target :
        remainder = n % 100
        answer += remainder
        break
    answer += target
    count +=1
print(answer)
'''
n = int(input())
ans = 0
start = 1
length =1
while start <= n:
    end = start * 10 -1
    if end > n:
        end = n
    ans += (end-start+1) * length
    start *= 10
    length += 1
print(ans)
