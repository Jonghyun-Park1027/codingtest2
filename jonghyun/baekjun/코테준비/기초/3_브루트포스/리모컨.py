'''
#unsovled : 구현실패 및 시간초과(recursive)
# 시간초과
n = int(input())
m = int(input())
if m == 0 :
    print(len(str(n)))
else : 
    erorr_button = list(map(int,input().split()))

button = [i for i in range(10)]
current = 100

for i in erorr_button:
    button.remove(i)

current_target = n - current # 최대 길이
ans = []
# for i in list(str(n)):
#     data = []
#     if i in button:
#         print(len(str(n)))
#     for i in list(str(n)):
#         # button.remove(i)
#         print(button)
#     else : # 이 때 경우의 수를 고려한다.
#         for i in button :
#             data.append(i)

# print(len(str(n)))
max_len = len(str(n))
count = 0
# max_target = int("".join([max(button)] * max_len))

def combine_elements(input_list, current='', index=0):
    if index == len(input_list):
        return [current]
    
    # 현재 원소를 추가하지 않은 경우
    without_current = combine_elements(input_list, current, index+1)
    # 현재 원소를 추가한 경우
    with_current = combine_elements(input_list, current + input_list[index], index+1)
    
    return without_current + with_current

combinations = combine_elements(list(map(str,button)), index=max_len)
# print(combinations)

combinations = list(map(int,combinations[1:]))
data= []
for i in combinations:
    data.append(abs(n - int(i)))
print(data)
compare = min(data)
if compare >= current_target :
    print(compare)
else :
    print(current_target)'''
# 10으로 나눈다는 아이디어
n = int(input())
m = int((input()))
broken = [False] * 10
if m >0:
    a = list(map(int,input().split()))
else :
    a = []
for x in a:
    broken[x] = True
def possible(c):
    if c==0:
        if broken[0]:
            return 0
        else :
            return 1
    l = 0
    while c >0 :
        if broken[c%10]:
            return 0
        l += 1
        c//= 10
    return l
ans = abs(n-100)
for i in range(0,1000000+1):
    c = i
    l = possible(c)
    if l > 0 :
        press = abs(c-n)
        if ans > l + press:
            ans = l+press
print(ans)