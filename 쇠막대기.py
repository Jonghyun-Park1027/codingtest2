g = input()


# print(g)

# 레이져로 자르는 절단부위 만들기
pipe = []
count = 0

# 인덱스를 기준으로 파이프 갯수를 저장할 리스트


for i, v in enumerate(g):
    # 절단 부분이 생길 때
    if v == '(':
        pipe.append(i)
    else :

        if pipe and pipe[-1] + 1 == i:
            # 파이프 내에 파이프가 존재할 경우 계속 자른다
            
            pipe.pop()
            count += len(pipe)
                # print("act")
# 파이프 만들기, 길이를 고려하지 않았을 경우, 단순히 있다 없다정도로 갯수를 넣는다
        else :
            if pipe:

                pipe.pop()
            count += 1
print(count)

    