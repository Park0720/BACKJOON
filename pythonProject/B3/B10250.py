T = int(input())

for test_case in range(1, T+1):
    H, W, N = map(int, input().split())

    floor = N % H
    room = N // H + 1
    if floor == 0:
        room -= 1
        floor = H

    print(100 * floor + room)