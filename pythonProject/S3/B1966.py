from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    important_list = list(map(int, input().split()))
    queue = deque()
    for _ in range(N):
        queue.append(_)

    while len(queue) > 0:
        for important in important_list:
            if important > important:
                pass
