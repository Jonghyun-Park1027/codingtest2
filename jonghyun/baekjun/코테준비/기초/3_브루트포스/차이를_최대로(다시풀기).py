n = int(input())
a = list(map(int, input().split()))
a.sort()
# print(a)
#


def per(a):
    i = len(a) - 1
    # a[i] > a[i-1]인 경우를 찾는다
    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False

    # j 는 a[i] 보다 작고, 나머지에서 가장 큰수여야함
    #
    j = len(a) - 1
    while a[i-1] >= a[j]:
        j -= 1
    # i를 기준으로 i-1(다음 수열인 것)과 j(i를 제외한 나머지에서 갖아 큰 수 인덱스)를 스왑해줌

    a[j], a[i-1] = a[i-1], a[j]

    # j를 역순으로 올라가면서 i와 j의 데이터들을 바꿔줌
    j = len(a)-1
    while j >i:
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1
    return True

def cal(a):
    cnt = 0
    for i in range(1, len(a)):
        cnt += abs(a[i] - a[i-1])
    return cnt
answer = 0
while True:
    # print(' '.join(map(str, a)))
    # cnt = 0
    cnt = cal(a)
        # print(i)
    answer = max(answer, cnt)
    # print(cnt)
# per(a)
    if not per(a):
        break
print(answer)
# print(a)
