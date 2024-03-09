def bfs(maps, visited):
    queue = []
    # 큐에 시작 지점 담아줌
    queue.append([start_row, start_col])
    # 시작 지점의 간선 수 0으로 초기화
    visited[start_row][start_col] = 0

    # 큐가 비어 있지 않으면
    while queue:
        # 현재 위치 설정
        current = queue.pop(0)
        # 현재 위치의 좌표 설정
        c_row, c_col = current[0], current[1]
        for k in range(4):
            # 4방향 탐색 및 탐색 조건
            n_row = c_row + dr[k]
            n_col = c_col + dc[k]
            if (0 <= n_row < N and 0 <= n_col < M) and maps[n_row][n_col] == 1:
                # 방문하지 않았고, maze 에서 갈 수 있는 길일 경우
                if visited[n_row][n_col] == 0 and maps[n_row][n_col] == 1:
                    # 큐에 인접 정점 삽입
                    queue.append([n_row, n_col])
                    # 다음 위치에 현재 위치 + 1 해서 간선 수 추가
                    visited[n_row][n_col] = visited[c_row][c_col] + 1




N, M = map(int, input().split())
maze_list = [list(map(int, input().split())) for _ in range(N)]
# 간선 수를 알아낼 미로와 같은 크기의 배열
visited = [[0] * M for _ in range(N)]

# 시작 지점, 끝 지점 초기화
start_row, start_col = 0, 0

for i in range(N):
    for j in range(M):
            # 시작 지점 찾기
            if maze_list[i][j] == 2:
                start_row, start_col = i, j

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

bfs(maze_list, visited)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and maze_list[i][j] == 1:
            visited[i][j] = -1
# 간선 수는 답안에서 -1 뺀 값

for i in range(N):
    print(*visited[i])
