# print(120//10)
n = int(input())
ans = 0
num = 1
num_len= 1
while  num <= n:
    end = num*10-1
    if end > n:
        end = n
    ans += (end-num+1)*num_len
    num *= 10
    num_len += 1
print(ans)