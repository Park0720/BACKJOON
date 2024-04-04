import sys
from copy import deepcopy
from collections import deque


def brute_force(x):
    global count, max_virus, visited
    if x == 3:
        count = 0
        copy_list = deepcopy(base_list)
        visited = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if copy_list[i][j] == 2 and visited[i][j] == 0:
                    bfs(i, j, copy_list)

        for i in range(N):
            for j in range(M):
                if copy_list[i][j] == 0:
                    count += 1
        if max_virus < count:
            max_virus = count
        return

    for i in range(N):
        for j in range(M):
            if base_list[i][j] == 0:
                base_list[i][j] = 1
                brute_force(x+1)
                base_list[i][j] = 0


def bfs(start_row, start_col, arr):
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = 1
    while queue:
        cur_row, cur_col = queue.popleft()
        for k in range(4):
            new_row = cur_row + dr[k]
            new_col = cur_col + dc[k]
            if 0 <= new_row < N and 0 <= new_col < M and arr[new_row][new_col] == 0:
                arr[new_row][new_col] = 2
                visited[new_row][new_col] = 1
                queue.append((new_row, new_col))


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, sys.stdin.readline().split())
base_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
count = 0
max_virus = 0

brute_force(0)
print(max_virus)
