import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()

for i in range(N):
    order_list = list(map(str, sys.stdin.readline().split()))
    if len(order_list) == 2:
        order, value = order_list[0], int(order_list[1])
    else:
        order = order_list[0]

    if order == 'push_front':
        deq.appendleft(value)

    if order == 'push_back':
        deq.append(value)

    if order == 'pop_front':
        if len(deq) > 0:
            sys.stdout.write(str(deq.popleft()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')

    if order == 'pop_back':
        if len(deq) > 0:
            sys.stdout.write(str(deq.pop()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')

    if order == 'size':
        sys.stdout.write(str(len(deq)) + '\n')

    if order == 'empty':
        if len(deq) == 0:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')

    if order == 'front':
        if len(deq) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(deq[0]) + '\n')

    if order == 'back':
        if len(deq) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(deq[-1]) + '\n')
