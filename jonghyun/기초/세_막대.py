data = list(map(int,input().split()))

max_idx = data.index(max(data))
max_data = max(data)
sum_rest = 0
for i in range(3):
    if i != max_idx:
        sum_rest += data[i]
a,b,c = data

if a== b and b== c and a==c :

    print(sum(data))
elif max_data < sum_rest :
    print(sum(data))
elif max_data >= sum_rest:
    while max_data >= sum_rest :
        max_data -= 1
    print(max_data + sum_rest)
    
