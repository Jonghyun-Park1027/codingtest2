from datetime import datetime, timedelta

# True로 초기화해야하나
from collections import defaultdict

# 조건 매주 5회 이상, 매주 총 60시간이면 True
answer = defaultdict(lambda: True)
time = defaultdict(lambda: timedelta(0))
day = defaultdict(lambda: 0)
n, m = map(int, input().split())  # 1<=n <= 36400 , 7 <= m <= 364
week_task = 5
week_time_task = timedelta(hours=60)
for _ in range(n):
    s = input().split()
    s[2] = datetime.strptime(s[2], "%H:%M")
    s[2] = timedelta(hours=s[2].hour, minutes=s[2].minute)
    s[3] = datetime.strptime(s[3], "%H:%M")
    s[3] = timedelta(hours=s[3].hour, minutes=s[3].minute)
    broad = s[3] - s[2]
    key = s[0]
    checker = int(s[1])  # 이거 7로 모듈러스해야함
    time[key] += broad
    day[key] += 1
    if checker % 7 == 0:
        # print(time)
        for i in day:
            # print(i, time[i])
            if time[i] >= week_time_task and day[i] >= week_task:
                answer[i] = answer[i] and True
            else:
                answer[i] = answer[i] and False


option = False
for k in sorted(answer):
    if answer[k]:
        option = True
        print(k)

if not option:
    print(-1)
