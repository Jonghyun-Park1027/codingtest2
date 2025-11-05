n, m = map(int, input().split())
a = list(map(int, input().split()))  # A-B
b = list(map(int, input().split()))  # B-A

a.sort(reverse=True)
b.sort(reverse=True)

# 체인의 최대 길이
k = min(n, m + 1)

# 번갈아가며 연결
total_a_outlets = 0
for i in range(k):
    if i % 2 == 0:
        # A-B 멀티탭 선택 (A 콘센트 → B 콘센트 제공)
        total_a_outlets -= 1  # 이 멀티탭을 연결하기 위해 A 콘센트 하나 소비
    else:
        # B-A 멀티탭 선택 (B 콘센트 → A 콘센트 제공)
        total_a_outlets += b[i // 2]  # B-A는 A 콘센트를 만들어냄

# 시작 A 콘센트 1개 + 총 변화량
print(1 + total_a_outlets)
