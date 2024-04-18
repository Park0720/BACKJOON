import sys
from collections import deque


def bfs(sr, sc):
    global shake_big
    can_eat = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    queue = deque([(sr, sc)])
    visited[sr][sc] = 1
    eat = []
    while queue:
        cr, cc = queue.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            # 아기 상어가 이동할 수 있는 지역 탐색
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and base_list[nr][nc] <= shake_big:
                visited[nr][nc] = visited[cr][cc] + 1
                queue.append((nr, nc))
                # 아기 상어가 이동할 수 있는 지역 중에서 먹을 수 있는 물고기가 있는 곳
                if base_list[nr][nc] < shake_big and base_list[nr][nc]:
                    # 시작 지점을 무조건 1로 설정해서 도달할 수 있는 시간은 -1 로 설정
                    can_eat[nr][nc] = visited[nr][nc] - 1
                    # 상어가 먹을 수 있는 물고기 거리, 위치 리스트
                    eat.append((can_eat[nr][nc], nr, nc, base_list[nr][nc]))

    # 먹을 수 있는 물고기가 여러개고, 같은 거리 일 경우 가장 위의, 가장 위인 물고기가 많으면 가장 왼쪽의 물고기를 먹음
    eat = sorted(eat, key=lambda x: (x[0], x[1], x[2]))
    return eat


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N = int(sys.stdin.readline())

base_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shake_big = 2
eat_count = 0
answer = 0

# 아기 상어의 첫 위치 탐색
start_row, start_col = 0, 0
for i in range(N):
    for j in range(N):
        if base_list[i][j] == 9:
            start_row, start_col = i, j

# 모든 물고기를 다 먹을 때까지
while True:
    # bfs 리턴 값 받아오기
    eat_point = deque(bfs(start_row, start_col))
    # 먹을 수 있는 물고기가 없으면 break
    if not eat_point:
        break

    # 먹을 물고기는 받아온 리스트 중 첫 번째 물고기
    dis, current_row, current_col, size = eat_point.popleft()
    answer += dis
    eat_count += 1

    # 아기 상어가 자라는 순간
    if shake_big == eat_count:
        shake_big += 1
        eat_count = 0

    # 물고기 먹었음 처리
    base_list[start_row][start_col] = 0
    # 물고기를 먹고 아기 상어의 위치 재설정
    start_row, start_col = current_row, current_col

print(answer)