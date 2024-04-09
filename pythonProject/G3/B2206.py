import sys
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(N, M, arr):
    queue = deque([(0, 0, 1)])  # (행, 열, 벽을 부순 횟수)
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]  # 방문 여부 및 벽을 부쉈는지의 여부를 저장

    visited[0][0][1] = 1  # 시작 지점 방문 표시

    while queue:
        r, c, wall_broken = queue.popleft()

        if r == N-1 and c == M-1:  # 목적지에 도착한 경우
            return visited[r][c][wall_broken]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and wall_broken:  # 다음 칸이 벽이고, 아직 벽을 부수지 않은 경우
                    visited[nr][nc][0] = visited[r][c][1] + 1
                    queue.append((nr, nc, 0))  # 벽을 부수고 이동
                elif arr[nr][nc] == 0 and visited[nr][nc][wall_broken] == 0:  # 다음 칸이 벽이 아니고, 방문하지 않은 경우
                    visited[nr][nc][wall_broken] = visited[r][c][wall_broken] + 1
                    queue.append((nr, nc, wall_broken))  # 벽을 부수지 않고 이동

    return -1  # 도착하지 못한 경우


N, M = map(int, sys.stdin.readline().split())
base_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

result = bfs(N, M, base_list)
print(result)
