import sys
real = "Stan may be honest"
fake = "Stan is dishonest"
high = 10
low = 1
t = []
answer = True

while True:
    num = int(input())
    # 숫자가 0이면 바로 나간다
    if num == 0:
        break
    
    stan = input().strip()
    # 스탠이 말한게 right on이라면
    if stan == "right on":
        if low <= num <= high and answer:
            t.append(True)
        else:
            t.append(False)
        # 다음 라운드를 위해 초기화
        high = 10
        low = 1
        answer = True

    elif stan == "too high":
        if num <= low:
            answer = False
            continue
        high = min(high, num - 1)  # high의 값을 num보다 하나 낮게 설정

    elif stan == "too low":
        if num >= high:
            answer = False
            continue
        low = max(low, num + 1)  # low의 값을 num보다 하나 높게 설정

# 결과 출력
for i in t:
    if i:
        print(real)
    else:
        print(fake)
