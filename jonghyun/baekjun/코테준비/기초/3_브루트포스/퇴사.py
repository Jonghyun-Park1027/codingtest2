# inf = -10**9
n = int(input())
days= [0] * (n+1)
pays = [0] * (n+1)

for i in range(1, n+1):
    d, p = map(int,input().split())
    days[i]=d
    pays[i]=p

# print(days, pays)

max_pay = 0
def cal(today,get):
    global max_pay
    if today> n+1 :
        return 
    # if today == n :
    if today == n+1 :
        max_pay = max(max_pay, get)
        return

    # for i in range(1, n+1):
        # today += days[i]
        # get += pays[i]
        
        # print(get, today)
    cal(today+1,get)
    cal(today+days[today], get+pays[today])

cal(1,0)
print(max_pay)