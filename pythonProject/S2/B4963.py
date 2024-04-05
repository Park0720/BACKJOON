import sys
from collections import deque


def bfs(start_row, start_col):
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = 1

    while queue:
        cr, cc = queue.popleft()
        for k in range(8):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == 0 and base_list[nr][nc] == 1:
                visited[nr][nc] = 1
                queue.append((nr, nc))


dr = [1, 0, -1, 0, 1, -1, 1, -1]
dc = [0, 1, 0, -1, 1, -1, -1, 1]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    base_list = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if base_list[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                count += 1

    print(count)