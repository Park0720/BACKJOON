import sys
from collections import deque

def bfs(sr, sc):
    global count
    queue = deque([(sr, sc)])
    visited[sr][sc] = count

    while queue:
        cr, cc = queue.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0 and base_list[nr][nc] == 0:
                visited[nr][nc] = count
                queue.append((nr, nc))


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
M, N, K = map(int, sys.stdin.readline().split())

base_list = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
count = 1


for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            base_list[i][j] = 1

for i in range(M):
    for j in range(N):
        if base_list[i][j] == 0 and visited[i][j] == 0:
            bfs(i, j)
            count += 1

count_list = [0] * count

for i in range(M):
    for j in range(N):
        for k in range(1, len(count_list)):
            if visited[i][j] == k:
                count_list[k] += 1

count_list.sort()
print(count-1)
for i in range(1, len(count_list)):
    print(count_list[i], end=' ')