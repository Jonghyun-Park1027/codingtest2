import sys
m = int(sys.stdin.readline())
# S = 0
# b = 1
# S = S | b
# print(S)
# S = bin(20 >> 2)
# print(S)
S = 0
t = 20
# print(S | 1)
for _ in range(m):
    action = sys.stdin.readline().split()
    # print(action)
    if action[0] == "all":
        S = (1 << t) -1

    elif action[0] == "empty":
        S = 0

    else :
        action, n = action
        n = int(n)-1
        if action == "add":
            S = (S | (1 << n))
        elif action == "remove":
            S = (S & ~(1 << n))
        elif action == "check":
            res = S & (1<<n)
            if res > 0 :
                print('1', end = "\n")
            else :
                print('0', end='\n')
        elif action == "toggle":
            S = S ^(1 << n)

# print( "?",(1 << n ) -1)
# print("S:",S)