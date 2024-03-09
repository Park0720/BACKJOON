import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()

for i in range(N):
    order_list = list(map(int, sys.stdin.readline().split()))
    if len(order_list) == 2:
        order, value = order_list[0], order_list[1]
    else:
        order = order_list[0]

    if order == 1:
        deq.appendleft(value)

    if order == 2:
        deq.append(value)

    if order == 3:
        if len(deq) > 0:
            sys.stdout.write(str(deq.popleft()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')

    if order == 4:
        if len(deq) > 0:
            sys.stdout.write(str(deq.pop()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')

    if order == 5:
        sys.stdout.write(str(len(deq)) + '\n')

    if order == 6:
        if len(deq) == 0:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')

    if order == 7:
        if len(deq) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(deq[0]) + '\n')

    if order == 8:
        if len(deq) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(deq[-1]) + '\n')
