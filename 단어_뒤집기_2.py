
words = input().split()  # 입력 받기

for word in words:
    raw_word = []  # 태그가 아닌 문자를 저장할 리스트
    tag_word = []  # 태그 문자를 저장할 리스트
    idx = 0
    tag = False  # 현재 태그 내부인지 여부를 나타내는 플래그
    while idx < len(word):
        ch = word[idx]
        if ch == "<":
            # 태그 시작 전까지의 문자들을 역순으로 출력
            while raw_word:
                print(raw_word.pop(), end="")
            tag = True
            tag_word.append(ch)
        elif ch == ">":
            tag = False
            tag_word.append(ch)
            # 태그 문자들을 그대로 출력
            while tag_word:
                print(tag_word.pop(0), end="")
        elif tag:
            # 태그 내부 문자 처리
            tag_word.append(ch)
        else:
            # 태그 외부 문자 처리
            raw_word.append(ch)
        idx += 1

    # 남은 태그가 아닌 문자들을 역순으로 출력
    while raw_word:
        print(raw_word.pop(), end="")

    print(" ", end="")  # 단어 사이 공백 출력

print()  # 줄바꿈 출력

