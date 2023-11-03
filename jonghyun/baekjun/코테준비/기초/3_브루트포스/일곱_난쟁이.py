data = []
for _ in range(9):
    data.append(int(input()))
answer = sum(data)
for idx_1, value_1 in enumerate(data):
    for idx_2, value_2 in enumerate(data):
        if idx_2 == idx_1 :

            continue
        elif answer - (value_1+ value_2) == 100:
            # print(idx_1,idx_2)<
            # break
            # data.remove(value_1)
            # data.remove(value_2)
            # print(value_1,value_2)
            a = value_1
            b = value_2
            break
    
    # print(value_1)
data.remove(a)
data.remove(b)
# print(data.pop(1))
data.sort()
print(*data, sep="\n")
# print(sum(data))