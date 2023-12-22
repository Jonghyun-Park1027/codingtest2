''' 오답: 시간초과(50분)
# a = {"a": 1}
# print(a.pop("a")) 1
# print(a) 1

# 테스트케이스 숫자를 받는다
n = int(input())

for _ in range(n):
    N, M = map(int,input().split())# N은 문서의 수 M은 찾는 문서의 번호
    data = list(map(int,input().split()))
    max_data = max(data)
    target_dict = {}
    for i in range(len(data)):
        target_dict[i] = data[i]

    # target_dict를 max값과 비교하여 재정렬한다
    for i in target_dict:
        if target_dict[i] == max_data:
            break
        d = target_dict.pop(0)
        target_dict[i] = d
        print(target_dict)
        '''
# a = [(2,0), (1,1), (4,2), (3,3)]
# print(max(a, key=lambda x: x[0]))

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x : x[0])[0]:
            count +=1
            if queue[0][1] == m :
                print(count)
                break
            else :
                queue.pop(0)
        else :
            queue.append(queue.pop(0))