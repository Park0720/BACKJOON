import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    order_list = list(map(str, sys.stdin.readline().split()))
    if len(order_list) == 2:
        order, value = order_list[0], int(order_list[1])
    else:
        order = order_list[0]

    if order == 'push':
        queue.append(value)

    if order == 'pop':
        if len(queue) > 0:
            sys.stdout.write(str(queue.pop(0)) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')

    if order == 'size':
        sys.stdout.write(str(len(queue)) + '\n')

    if order == 'empty':
        if len(queue) == 0:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')

    if order == 'front':
        if len(queue) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(queue[0]) + '\n')

    if order == 'back':
        if len(queue) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(queue[-1]) + '\n')
