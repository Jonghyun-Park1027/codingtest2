import sys
MAX = 1000001
check = [0]*MAX
check[1]= check[0] = 1
data = []
for i in range(2,MAX):
    if check[i] == 0:
        data.append(i)
        j = i+i
        while j<MAX:
            check[j] = 1
            j +=i
while True:
    try :
        n = int(sys.stdin.readline())
        for i in data:
            a = n-i

            if check[a] == 0:
                print(f"{n} = {i} + {a}")
                break
    except:
        exit()
# print(data)