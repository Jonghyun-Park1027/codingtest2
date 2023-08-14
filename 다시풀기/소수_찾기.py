'''
반동 : test케이스만 통과
n = int(input())
data = list(map(int,input().split()))
answer = 0
for i in data:

    count= 0
    for j in range(2, i):
        if i %j != 0:
            count = True
        else :
            count = False
    answer += count
print(answer)'''

'''
다른풀이
def is_prime(x):
    if x <2:
        return False
    i = 2
    while i*i <= x:
        if x% i ==0:
            return False
        i += 1
    return True

n = int(input())
a = list(map(int,input().split()))
ans =0
for x in a:
    if is_prime(x):
        ans +=1
print(ans)'''
# 리스트 초기화
MAX = 1001
check = [0]* MAX
check[0]= check[1] = 1
# check 순환하기
for i in range(2,MAX):
    
    if check[i]== 0:
        j = i+i
        while j<MAX:
            check[j]=1
            j+=i
n = int(input())
data = list(map(int,input().split()))
count = 0
for i in data:
    if check[i]== 0:
        count += 1
print(count)

# 소수 찾기