N = int(input())

for i in range(1, N + 1):
    if i < N:
        print(' ' * (N - (i + 1)), end=' ')
    for j in range(0, 2*i-1):
        print('*', end='')
    print()