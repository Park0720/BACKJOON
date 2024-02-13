N = int(input())

for i in range((N + 1) - 1, 1, -1):
    if i < (N + 1):
        print(' ' * ((N + 1) - (i+1)), end='')
    for j in range(0, 2*i-1):
        print('*', end='')
    print()
for i in range(1, (N + 1)):
    if i < (N + 1):
        print(' ' * ((N + 1) - (i+1)), end='')
    for j in range(0, 2*i-1):
        print('*', end='')
    print()