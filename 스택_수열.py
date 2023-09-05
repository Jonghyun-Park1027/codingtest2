import sys
n = int(input()) # 1 <= n <= 100000 
stack = []
ans = ''

now = 0

a = [int(input()) for _ in range(n)]
for x in a :
    if x>now :
        while x > now :
            now += 1
            stack.append(now)
            ans += '+\n'
        stack.pop()
        ans += '-\n'
    else :
        if stack[-1] != x:
            print("NO")
            sys.exit(0)
        stack.pop()
        ans += '-\n'
print(ans, end='')