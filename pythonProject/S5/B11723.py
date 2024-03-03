import sys

M = int(sys.stdin.readline())

base_set = set()
all_set = set(range(1, 21))

for _ in range(M):
    order_list = sys.stdin.readline().split()
    if len(order_list) == 2:
        order, value = order_list[0], int(order_list[1])
    else:
        order = order_list[0]

    if order == 'add':
        base_set.add(value)

    elif order == 'remove':
        base_set.discard(value)

    elif order == 'check':
        sys.stdout.write('1\n' if value in base_set else '0\n')

    elif order == 'toggle':
        if value in base_set:
            base_set.remove(value)
        else:
            base_set.add(value)

    elif order == 'all':
        base_set = all_set.copy()

    elif order == 'empty':
        base_set.clear()
