def bfs(x, y):
    global count
    visited[x][y] = count
    queue = [(x, y)]
    while queue:
        row, col = queue.pop(0)
        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]

            if (0 <= nr < N and 0 <= nc < M) and visited[nr][nc] == 0 and base_list[nr][nc] == 1:
                queue.append((nr, nc))
                visited[nr][nc] = count

    count += 1


T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())

    base_list = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 1

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for i in range(K):
        X, Y = map(int, input().split())
        base_list[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if base_list[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)

    print(count-1)
