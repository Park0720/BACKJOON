import heapq, sys

N = int(sys.stdin.readline().strip())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not heap:
            print(0)
            continue
        answer = heapq.heappop(heap)
        if answer[1]:
            # 1이면 그대로 출력
            print(answer[0])
        else:
            # 0이면 - 붙인 채 출력
            print(-answer[0])
    elif x > 0:
        # 양수면 그대로 넣고 1이라고 표기
        heapq.heappush(heap, [x, 1])
    else:
        # 음수면 - 붙인 채 넣고 0이라고 표기
        heapq.heappush(heap, [-x, 0])