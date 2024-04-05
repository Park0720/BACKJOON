import sys
from collections import deque
from copy import deepcopy


def bfs(start_row, start_col, color, arr):
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = 1

    while queue:
        cur_row, cur_col = queue.popleft()
        for k in range(4):
            nr = cur_row + dr[k]
            nc = cur_col + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] == color:
                visited[nr][nc] = 1
                queue.append((nr, nc))


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
color_list = ['R', 'G', 'B']
color_count = [0, 0, 0]
N = int(sys.stdin.readline())
base_list = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for c in range(len(color_list)):
    for i in range(N):
        for j in range(N):
            if base_list[i][j] == color_list[c] and visited[i][j] == 0:
                bfs(i, j, color_list[c], base_list)
                color_count[c] += 1

non_red_list = deepcopy(base_list)
visited = [[0] * N for _ in range(N)]

non_red = ['R', 'B']
non_red_count = [0, 0]
for i in range(N):
    for j in range(N):
        if non_red_list[i][j] == 'G':
            non_red_list[i][j] = 'R'

for c in range(len(non_red)):
    for i in range(N):
        for j in range(N):
            if non_red_list[i][j] == non_red[c] and visited[i][j] == 0:
                bfs(i, j, non_red[c], non_red_list)
                non_red_count[c] += 1


print(sum(color_count), sum(non_red_count))