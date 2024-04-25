import sys
from collections import deque


def bfs(sr, sc):
    visited = [[0] * M for _ in range(N)]
    queue = deque([(sr, sc)])
    visited[sr][sc] = 1
    count = 0

    while queue:
        cr, cc = queue.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc] == 'L':
                visited[nr][nc] = visited[cr][cc] + 1
                if visited[nr][nc] > count:
                    count = visited[nr][nc]
                queue.append((nr, nc))

    return count


N, M = map(int, sys.stdin.readline().split())
maps = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

answer = 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer - 1)