N = int(input())

# 중앙을 기점으로 위 아래 나눠서 출력
for i in range(1, (N + 1)):
    if i < N + 1:
        print(' ' * ((N + 1) - (i + 1)), end='')
    for j in range(0, 2 * i - 1):
        print('*', end='')
    print()
for i in range((N - 1), 0, -1):
    if i < N + 1:
        print(' ' * ((N + 1) - (i + 1)), end='')
    for j in range(0, 2 * i - 1):
        print('*', end='')
    print()