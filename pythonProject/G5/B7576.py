import sys
from collections import deque


def bfs():
    while queue:
        cur_row, cur_col = queue.popleft()
        for k in range(4):
            new_row = cur_row + dr[k]
            new_col = cur_col + dc[k]
            if 0 <= new_row < N and 0 <= new_col < M and visited[new_row][new_col] == 0 and base_list[new_row][new_col] == 0:
                visited[new_row][new_col] = visited[cur_row][cur_col] + 1
                queue.append((new_row, new_col))


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
M, N = map(int, sys.stdin.readline().split())
base_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if base_list[i][j] == 1 and visited[i][j] == 0:
            queue.append((i, j))

bfs()

flag = False
answer = 0

for i in range(N):
    if answer < max(visited[i]):
        answer = max(visited[i])

for i in range(N):
    for j in range(M):
        if base_list[i][j] == 0 and visited[i][j] == 0:
            answer = -1
            flag = True
            break
    if flag:
        break

print(answer)