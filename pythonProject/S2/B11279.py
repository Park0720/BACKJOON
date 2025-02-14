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
        print(-answer)
    else:
        heapq.heappush(heap, -x)