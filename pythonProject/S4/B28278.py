import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    order_list = list(map(int, sys.stdin.readline().split()))
    if len(order_list) == 2:
        order, value = order_list[0], order_list[1]
    else:
        order = order_list[0]

    if order == 1:
        stack.append(value)

    if order == 2:
        if len(stack) > 0:
            sys.stdout.write(str(stack.pop()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')

    if order == 3:
        sys.stdout.write(str(len(stack)) + '\n')

    if order == 4:
        if len(stack) == 0:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')

    if order == 5:
        if len(stack) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(stack[-1]) + '\n')
