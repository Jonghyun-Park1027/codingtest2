button = [i for i in range(9, -1, -1)]
now = 100
channel = int(input())
n = int(input())
broken = [False] * 10
if n > 0:
    a= list(map(int,input().split()))
    
else :
    a = []
for x in a:
    broken[x] = True

def possible(c):
    if c == 0 :
        if broken[0]:
            return 0
        else :
            return 1
    l = 0
    while c>0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l


# channel - 
# # print(button)
# target = list(map(int,str(channel)))
# print(target)
ans = abs(channel - now)
num = 1
for i in range(0, 1000000+1):
    # idx, i)
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-channel)
        if ans > l + press:
            ans = l+press
    # for j in button:
    #     if i-j >= 0:
    #         data.append(i-j)
    #         # print(j)
    #     else :
    #         data.append(i)
    #     # print(data)
    # target[idx] = min(data)
    # num += 1
# print(int(''.join(map(str,target)))+num)
# print()
print(ans)
