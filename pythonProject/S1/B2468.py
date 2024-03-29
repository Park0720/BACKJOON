from collections import deque


def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = 1

    while queue:
        now_row, now_col = queue.popleft()
        for k in range(4):
            nr = now_row + dr[k]
            nc = now_col + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and new_base[nr][nc] != 0:
                visited[nr][nc] = 1
                queue.append([nr, nc])


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


N = int(input())

base_list = [list(map(int, input().split())) for _ in range(N)]

_max = 0

for m in range(-1, 100):
    new_base = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if base_list[i][j] > m:
                new_base[i][j] = base_list[i][j]

    for i in range(N):
        for j in range(N):
            if new_base[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                count += 1
    if count > _max:
        _max = count

print(_max)
