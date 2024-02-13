T = int(input())

for i in range(T-1, -1, -1):
    print(' ' * i + '*' * (T-i), end='')
    print()