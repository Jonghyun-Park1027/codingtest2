# 에라토스테네스의 체

#m 과  n

m, n = map(int,input().split())

# 확인하는 배열
check = [0] + [0] * n

# 소수인지 확인하는 함수

# def prime(n):
#     if n <2 :
#         return False

#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             return False

#     return True



for i, v in enumerate(check):
    if i == 0 or i == 1 :
        continue
    elif v ==0:
        

        c = i
        c += i
        while c <=n:
            # print(c)
            check[c] = 1
            c += i
        # print(check)
check[0] = 1
check[1] = 1


for i, v in enumerate(check):
    if v == 0 and i >= m:
        print(i)

