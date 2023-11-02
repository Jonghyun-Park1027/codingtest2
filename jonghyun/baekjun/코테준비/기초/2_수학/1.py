
while True:
    try:
        n = int(input())
    except:
        break
    data = '1'
    count = 0
    while True:
        if int(data) % n != 0:

            data += '1'
            count += 1
        else :
            print(count+1)
            break
