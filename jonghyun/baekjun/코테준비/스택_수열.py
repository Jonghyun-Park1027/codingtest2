'''
오답 : 문제 이해를 잘못하여 시간 초과
# for문을 반복할 숫자의 갯수 받음
n = int(input())
# 배열을 만듦
data = [i for i in range(1,n-1)]
stack = []
array = []
answer = []
for i in range(n):
    array.append(i)

for i in data:
    stack.append(i)
    if stack[-1] == i:
        # answer.append("+")



# [4,3,6,8,]
'''

n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data :
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else :
        print("NO")
        exit(0)
print('\n'.join(result))