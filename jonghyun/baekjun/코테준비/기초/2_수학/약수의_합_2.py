''' 구현 아이디어를 몰라서 못품
# import math
n = int(input())
sum = 0

for i in range(1,n+1):
    data = int(i**(1/2))
    # print(data)
    
    for j in range(1, i+1):
        if i%j == 0:
            sum += i
            sum += i/j
        
            # print(sum)
print(sum)
'''

# 답
n = int(input())
sum = 0
for i in range(1,n+1):
    sum+=n//i*i
print(sum)