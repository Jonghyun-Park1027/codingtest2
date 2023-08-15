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

max_target = n - current # 최대 길이
ans = []
for i in list(str(n)):
    data = []
    if i in button:
        print(len(str(n)))
    for i in list(str(n)):
        # button.remove(i)
        print(button)
    else : # 이 때 경우의 수를 고려한다.
        for i in button :
            data.append(i)
