import sys
from collections import deque

dh = [1, 0, -1, 0, 0, 0]
dr = [0, 1, 0, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

def ripe_tomato():
    while queue:
        ch, cr, cc = queue.popleft()
        for d in range(6):
            nh = ch + dh[d]
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and not ripe_days[nh][nr][nc] and not tomato_box[nh][nr][nc]:
                ripe_days[nh][nr][nc] = ripe_days[ch][cr][cc] + 1
                queue.append((nh, nr, nc))

input = sys.stdin.readline

M, N, H = map(int, input().strip().split())

tomato_box = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]

ripe_days = [[[0] * M for _ in range(N)] for _ in range(H)]

queue = deque()

# 익은 토마토 queue에 담아두기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_box[i][j][k] == 1:
                queue.append((i, j, k))

# 익기 시작
ripe_tomato()

# 못 익는 토마토 여부
flag = False

# 못 익는 토마토 체크
for i in range(H):
    for j in range(N):
        for k in range(M):
            if not tomato_box[i][j][k] and not ripe_days[i][j][k]:
                flag = True
                print(-1)
                break
        if flag:
            break
    if flag:
        break

# 다 익을 수 있는 경우 최댓값 출력
answer = 0
if not flag:
    for i in range(H):
        for j in range(N):
            if answer < max(ripe_days[i][j]):
                answer = max(ripe_days[i][j])

    print(answer)