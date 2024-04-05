import sys
from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1

    while queue:
        now = queue.popleft()
        for w in adjl[now]:
            if visited[w]:
                continue
            visited[w] = 1
            queue.append(w)


N, M = map(int, sys.stdin.readline().split())

adjl = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adjl[A].append(B)
    adjl[B].append(A)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
