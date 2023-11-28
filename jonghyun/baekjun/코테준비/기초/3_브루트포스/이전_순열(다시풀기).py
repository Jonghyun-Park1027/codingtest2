# 이제 거꾸로 해야함.
def next(a):
    # 순열 a의 길이를 역순으로 순회하게 한다
    i = len(a) - 1
    # a[i-1] >= a[i]를 만족하는 가장 큰 i를 찾는다.
    while i >0 and a[i-1] < a[i]:
        i -=1
    if i <= 0:
        return False
    # j < i 이면서 A[j] <= A[i-1]을 만족하는 가장 큰 j를 찾는다.
    j = len(a) - 1
    while j > 0 and a[j] > a[i-1] :
        j -= 1
        # print(j)
    # a[i-1]과 a[j]를 스왑한다
    a[i-1], a[j] = a[j], a[i-1]


    # a[i] 부터 순열을 뒤집는다.
    j = len(a) -1
    while i <= j-1 :
        a[i], a[j] = a[j], a[i]
        i += 1
        j -=1
    return True
n = int(input())
a = list(map(int, input().split()))
if next(a):
    print(*a)
else:
    print(-1)
# print(a)
# from itertools import per