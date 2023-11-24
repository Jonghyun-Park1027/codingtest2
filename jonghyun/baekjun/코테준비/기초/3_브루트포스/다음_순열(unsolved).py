

# n = int(input())

# data = list(map(int, input().split()))
# print(target)
# data = sorted(target)
# answer = data.copy()
# for i in range(n-1, 0, -1):
#     # print(i)
#     if data[i] <= data[i-1]:


#         # i가 끝까지 가면 -1를 출력하고 종료
#         if i-1 == 0:
#             print(-1)
#             break
#         continue
#     else:
#         # a = answer.index(min(list(filter(lambda x: x >= data[i], answer[i:]))))
#         # b = i-1
#         # answer[a], answer[b] = answer[b], answer[a]
#         answer = answer[:i-1]+answer[i-1:][::-1]
#         # print(list(filter(lambda x: x >= data[i], answer[i:])))
#         # print(answer.index(min(answer[i:])))
#         # print(i-1)
#         print(*answer)
#         break
# def next_permutation(a):
#     i = len(a) - 1
#     while i > 0 and a[i-1] >= a[i]:
#         i -= 1
#     if i <= 0:
#         return False
#     j = len(a) - 1
#     while a[j] <= a[i-1]:
#         j -= 1

#     a[i-1], a[j] = a[j], a[i-1]
#     j = len(a)-1
#     while i < j:
#         a[i], a[j] = a[j], a[i]
#         i += 1
#         j -= 1
#     return True


# n = int(input())
# a = list(map(int, input().split()))
# if next_permutation(a):
#     print(' '.join(map(str, a)))
# else:
#     print(-1)

def next(a):
    # 순열 a의 길이를 역순으로 순회하게 한다
    i = len(a) - 1
    # a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다.
    while i >0 and a[i-1] >= a[i]:
        i -=1
    if i <= 0:
        return False
    # j >= i 이면서 A[j] > A[i-1]을 만족하는 가장 큰 j를 찾는다.
    j = len(a) - 1
    while j > 0 and a[j] <= a[i-1] :
        j -= 1
    
    # a[i-1]과 a[j]를 스왑한다
    a[i-1], a[j] = a[j], a[i-1]


    # a[i] 부터 순열을 뒤집는다.
    j = len(a) -1
    while i <= j-1 :
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True
n = int(input())
a = list(map(int, input().split()))

if next(a):
    print(*a)
else:
    print(-1)