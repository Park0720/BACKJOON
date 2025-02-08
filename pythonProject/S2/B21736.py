import sys
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def meet_people(row, col):
    global meet_count
    visited[row][col] = 1
    queue = deque([(row, col)])
    while queue:
        row, col = queue.popleft()
        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and campus[nr][nc] != 'X':
                visited[nr][nc] = 1
                queue.append((nr, nc))
                if campus[nr][nc] == 'P':
                    meet_count += 1

N, M = map(int, sys.stdin.readline().strip().split())

campus = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cur_row, cur_col = 0, 0
find_i = 0
meet_count = 0

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            cur_row, cur_col = i, j
            find_i = 1
            break
    if find_i:
        break

meet_people(cur_row, cur_col)

if meet_count == 0:
    print('TT')
else:
    print(meet_count)
