import sys
from collections import deque


def bfs(sr, sc):
    queue = deque([(sr, sc)])
    count = 1
    visited[sr][sc] = count
    while queue:
        cr, cc = queue.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and base_list[nr][nc] == 1:
                visited[nr][nc] = count
                queue.append((nr, nc))
                count += 1
    return count


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().split())

base_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
count_paint = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if base_list[i][j] == 1 and visited[i][j] == 0:
            max_area = max(bfs(i, j), max_area)
            count_paint += 1

print(count_paint)
print(max_area)