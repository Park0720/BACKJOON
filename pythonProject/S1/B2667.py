import pprint

def bfs(maps, visited):
    global count
    queue = []
    # 큐에 시작 지점 담아줌
    queue.append([start_row, start_col])
    # 시작 지점의 간선 수 0으로 초기화
    visited[start_row][start_col] = count

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
            if (0 <= n_row < N and 0 <= n_col < N) and maps[n_row][n_col] == 1:
                # 방문하지 않았고, maze 에서 갈 수 있는 길일 경우
                if visited[n_row][n_col] == 0 and maps[n_row][n_col] == 1:
                    # 큐에 인접 정점 삽입
                    queue.append([n_row, n_col])
                    # 다음 위치에 현재 위치 + 1 해서 간선 수 추가
                    visited[n_row][n_col] = count

    count += 1


N = int(input())

maze_list = [list(map(int, input())) for _ in range(N)]
# 간선 수를 알아낼 미로와 같은 크기의 배열
visited = [[0] * N for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

count = 1
# 시작 지점, 끝 지점 초기화
for i in range(N):
    for j in range(N):
        if maze_list[i][j] == 1 and visited[i][j] == 0:
            start_row, start_col = i, j
            bfs(maze_list, visited)

print(count - 1)
home_count = [0] * count
for i in range(N):
    for j in range(N):
        for k in range(1, count):
            if visited[i][j] == k:
                home_count[k] += 1

home_count.pop(0)
home_count.sort()
print(*home_count, sep='\n')
