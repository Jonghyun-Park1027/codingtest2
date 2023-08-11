
'''
recursive 오류 : 1000번 이상 반복됨
import sys
def increase(data, target):

    if int(''.join(data)) % target == 0:
        return len(data)
    else :
        data.append('1')
        return increase(data,target)

while True:
    try:
        n = int(sys.stdin.readline())

    except:
        break
    print(increase(['1'],n))
'''
# solved
while True :
    try :
        data = ['1']
        n = int(input())

        while True :   
        
            if int(''.join(data)) % n == 0 :
                print(len(data))
                break
            else :
                data.append('1')

    except :
        break

# print(''.join(n))
''' 다른풀이
while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    while True:
        num = num * 10 + 1;
        num %= n
        if num == 0:
            print(i)
            break
        i += 1

'''
