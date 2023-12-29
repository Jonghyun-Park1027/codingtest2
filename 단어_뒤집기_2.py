def print_stack(s):
    while s:
        print(s.pop(), end='')

def main():
    str_input = input()
    tag = False
    stack = []

    for ch in str_input:
        if ch == '<':
            print_stack(stack)
            tag = True
            print(ch, end='')
        elif ch == '>':
            tag = False
            print(ch, end='')
        elif tag:
            print(ch, end='')
        else:
            if ch == ' ':
                print_stack(stack)
                print(ch, end='')
            else:
                stack.append(ch)

    print_stack(stack)
    print()

if __name__ == "__main__":
    main()
