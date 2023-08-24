'''def fact_1(n):
    if n > 1:
        return n * fact_1(n-1)
    return n
def fact_2(n):
    if n<=1:
        return n
    else :
        return n*fact_2(n-1)
    
print(fact_2(3))'''
n = int(input())
# check = [0]*(n+1)
# answer = [0]
count = 0
def cal(n, target):
    if n > target :
        return 0
    if target == n :
        # count += 1
        # print(count)
        return 1
    # loop = 1
    now = 0
    # while loop < 11:
    # for _ in range(10):
    for i in range(1,4):
        # if check[i] :
            # continue
        # check[i] = True

        now += cal(n+i, target)
        # check[i] = False
    return now
        # loop +=1
for _ in range(n):
    m = int(input())
    print(cal(0, m))

# print(count)

