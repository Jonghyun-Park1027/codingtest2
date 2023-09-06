import sys
n = int(sys.stdin.readline().strip())
queue = []
for _ in range(n):
    # [push X, pop, size, empty(1,0), front, back]
    what = sys.stdin.readline().split()
    if what[0] == 'push' :
        queue.append(what[1])
    elif what[0] == "pop" :
        if queue :
            i = queue.pop(0)
            print(i)
            
        else :
            print(-1)
    elif what[0] == "size" :
        print(len(queue))
    elif what[0] == "empty" :
        if queue :
            print(0)
        else :
            print(1)
    elif what[0] == "front" :
        if queue :
            print(queue[0])
        else :
            print(-1)
    elif what[0] == "back" :
        if queue :
            print(queue[-1])
        else :
            print(-1)