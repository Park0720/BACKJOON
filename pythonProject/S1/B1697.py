import sys
from collections import deque


def bfs(x, count):
    queue = deque([(x, count)])
    while queue:
        now, now_count = queue.popleft()
        if now == K:
            return now_count
        if now in visited:
            continue
        visited.add(now)
        if 0 <= now-1 <= 100000:
            queue.append((now-1, now_count+1))
        if 0 <= now + 1 <= 100000:
            queue.append((now+1, now_count+1))
        if 0 <= now * 2 <= 100000:
            queue.append((now*2, now_count+1))


N, K = map(int, sys.stdin.readline().split())
visited = set()

print(bfs(N, 0))
