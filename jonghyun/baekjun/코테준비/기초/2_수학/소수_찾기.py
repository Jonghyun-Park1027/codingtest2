T= int(input())
data = list(map(int,input().split()))
for i in data:
    if i == 1 :
        T -= 1
        continue
    for j in range(2, i+1):
        if j*j > i:
            break
        elif i % j == 0:
            T -= 1
            break

print(T)